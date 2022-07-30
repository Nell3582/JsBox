"""
@author: pysta feat by senku
@file: RequestToJs.py
@createTime: 2020-05-01
@updateTime: 2020-05-04
@description: 根据 Surge or Thor 请求内容生成相应的 js 请求脚本 兼容Surge&&Qx
并没有写通知
"""

import zipfile
import json
import appex
import clipboard
import console
from urllib3.filepost import encode_multipart_formdata as emf
import argparse
import re
import shlex


def parse_curl(curl_command):
  parser = argparse.ArgumentParser()
  parser.add_argument('command')
  parser.add_argument('url')
  parser.add_argument('-d', '--data')
  parser.add_argument('--data-raw', default='')
  parser.add_argument('-b', '--data-binary', default=None)
  parser.add_argument('-X', default='')
  parser.add_argument('-k', action="store_true")
  parser.add_argument('-L', action="store_true")
  parser.add_argument('-H', '--header', action='append', default=[])
  parser.add_argument('--compressed', action='store_true')
  parser.add_argument('--insecure', action='store_true')
  
  
  method = "get"
  tokens = shlex.split(curl_command)
  parsed_args = parser.parse_args(tokens)

  post_data = parsed_args.data or parsed_args.data_binary or parsed_args.data_raw
  if post_data:
      method = 'post'

  if parsed_args.X:
      method = parsed_args.X.lower()
  url = parsed_args.url
  body = post_data if post_data else ''
  headers = {}
  for curl_header in parsed_args.header:
      if curl_header.startswith(':'):
          occurrence = [m.start() for m in re.finditer(':', curl_header)]
          header_key, header_value = curl_header[:occurrence[1]], curl_header[occurrence[1] + 1:]
      else:
          header_key, header_value = curl_header.split(":", 1)

      headers[header_key] = header_value.strip()

  return url, body, headers, method


def parse(path): 
  
  def parse_har():
    with open(path, 'r', encoding='utf-8') as f:
      d = json.load(f)['log']['entries'][
    0]['request']
      
    url = d['url']
    headers = {i['name']: i['value'] for i in d['headers']}
    params = d.get('postData',{}).get('params', '')
    if params:
      _ = [(i['name'], i.get('value', '')) for i in params]
      content,headers['Content-Type'] = emf(_)
      body = str(content, encoding='utf-8')
    else:
      body = d.get('postData', {}).get('text', '')    
    method = d['method'].lower()
    
    return url, body, headers, method
    
  def parse_qx():
  
    with open(f'{path}/0/basic') as f:
      url = f.read()
    with open(f'{path}/0/request_body') as f:
      body = f.read()
    with open(f'{path}/0/request_headers') as f:
      temp = f.read()
      method = temp.split()[0].lower()
      headers = {k:v for k, v in [i.split(': ',1) for i in temp.split('\n')[1:] if i]}
    
    return url, body, headers, method
  
  def parse_surge():
  
    with zipfile.ZipFile(path, 'r') as z:
      with z.open('model.json') as f:
        d = json.load(f)
      if 'request.dump' in z.namelist():
        with z.open('request.dump') as f:
          d['reqBody'] = f.read().decode('utf-8')
    
    url = d['URL']
    body = d.get('reqBody', '')
    method = d['method'].lower()
    headers = {k:v for k, v in [i.split(': ',1) for i in d['requestHeader'].split('\r\n')[1:] if i]}
    
    return url, body, headers, method
  
  if path.endswith('.har'):
    return parse_har()
  elif path.endswith('.zip'):
    return parse_surge()
  else:
    return parse_qx()
    
def main():
  curl = appex.get_text()
  if curl:
    url, body, headers, method = parse_curl(curl)
  else:
    path = appex.get_file_path()
    url, body, headers, method = parse(path)
  
  js = f'''
  const senku=init()
  const jsName="签到APP名称"
  const datastr=JSON.stringify(data) //可选项
  const url = {json.dumps(url)};
  const body = {json.dumps(body)};
  const headers = {json.dumps(headers, indent=4)};
  const request = {{
      url: url,
      headers: headers,
      body: body
  }};
  
  senku.{method}(request, function(error, response, data) {{
      try {{
      	senku.log(data)
          const reg = /匹配的正则表达式/;
          const ContinueSignDay = datastr.match(/a/)[1];
          const SignPoints = datastr.match(/b/)[1];
          const AllPoint = datastr.match(/c/)[1]; 
          senku.log("连续签到天数为" + ContinueSignDay,"本次签到共获得积分数" + SignPoints,"现有的总积分数为" + AllPoint)

          if(datastr.match(reg)){{
          //这儿加入一些自己想自定义的参数，主要是用来获取签到获得的积分或金币数，可能需要正则判断
          $senku.notify(jsName, "签到成功", "签到获得 " + coin[1] + " 金币")
          }}
          else if(datastr.match(reg2)){{
          $senku.notify(jsName, "重复签到", "今天已经签过到了")
          }}
          else{{
          $senku.notify(jsName, "签到失败", "cookie可能失效了")
          }}
          senku.done();
          
      }} catch(e) {{
          senku.log(e)
          senku.done();
      }}
  }});
  '''
  js=js+'''
  function init() {
    isSurge = () => {
        return undefined === this.$httpClient ? false : true
    }
    isQuanX = () => {
        return undefined === this.$task ? false : true
    }
    getdata = (key) => {
        if (isSurge()) return $persistentStore.read(key)
        if (isQuanX()) return $prefs.valueForKey(key)
    }
    setdata = (key, val) => {
        if (isSurge()) return $persistentStore.write(key, val)
        if (isQuanX()) return $prefs.setValueForKey(key, val)
    }
    msg = (title, subtitle, body) => {
        if (isSurge()) $notification.post(title, subtitle, body)
        if (isQuanX()) $notify(title, subtitle, body)
    }
    log = (message) => console.log(message)
    get = (url, cb) => {
        if (isSurge()) {
            $httpClient.get(url, cb)
        }
        if (isQuanX()) {
            url.method = 'GET'
            $task.fetch(url).then((resp) => cb(null, resp, resp.body))
        }
    }
    post = (url, cb) => {
        if (isSurge()) {
            $httpClient.post(url, cb)
        }
        if (isQuanX()) {
            url.method = 'POST'
            $task.fetch(url).then((resp) => cb(null, resp, resp.body))
        }
    }
    done = (value = {}) => {
        $done(value)
    }
    return {
        isSurge,
        isQuanX,
        msg,
        log,
        getdata,
        setdata,
        get,
        post,
        done
    }
}
  '''
  print(js)
  clipboard.set(js)
  console.hud_alert('Copyed!')
  
if __name__ == '__main__':
  if appex.is_running_extension():
    main()
  else:
    print('请设置为 Share Extension 脚本后使用。')
