hostname = zsd.shuibiao100.cn,api.jinbangtech.cn,xqh5.17wanxiao.com,wfwapi.china-qzxy.cn,userapi.qiekj.com,dcxy-customer-app.dcrym.com,zxg.txfund.com,m.client.10010.com


# > hyl
http-request https://api\.jinbangtech\.cn//api/(SettleHotWaterOrder|CreateHotWaterOrder)(\d+)$ requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/hyl/hylRequest.js
http-response https://api\.jinbangtech\.cn//api/(SettleHotWaterOrder|CreateHotWaterOrder)(\d+)$ requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/hyl/hylResponse.js

# > wdsb
http-request https://zsd\.shuibiao100\.cn/water\-web\-portal/member/(getWallet|addPreConsume|addWaterConsume) requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/wdsb/getUserInfo.js, tag = 旺达水宝数据获取
http-response https://zsd\.shuibiao100\.cn/water\-web\-portal/member/(getWallet|addPreConsume|addWaterConsume) requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/wdsb/wdtest.js, tag = 旺达水宝用水

# > wmxy
http-request https:\/\/xqh5\.17wanxiao\.com\/BleWaterControlService\/(BLEUtil|WXInvokFront) requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/wmxy/wmxyRequest.js
http-response https:\/\/xqh5\.17wanxiao\.com\/BleWaterControlService\/(BLEUtil|WXInvokFront) requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/wmxy/wmxyResponse.js

# > qzxy
http-request https:\/\/wfwapi\.china\-qzxy\.cn/(.+)/upload/data requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/qzxy/getUserInfo.js, tag = (趣智校园)获取数据后右滑禁用,enabled = false
http-request https:\/\/wfwapi\.china\-qzxy\.cn\/(.+)/upload/data requires-body=1,max-size=0, script-path=https://gitee.com/Nell3582/Nell9382/raw/master/qzxy/qzxyRequest.js
http-response https:\/\/wfwapi\.china\-qzxy\.cn\/(.+)/upload/data requires-body=1,max-size=0, script-path=https://gitee.com/Nell3582/Nell9382/raw/master/qzxy/qzxyResponse.js

# > qexy
# http-request ^https:\/\/userapi\.qiekj\.com/unimkt/launch requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/qexy/qexyRequest.js
# http-response ^https:\/\/userapi\.qiekj\.com/(order/add|order/detail|order/preview|user/astrict/residue) requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/qexy/qexyResponse.js

# dcxy
http-response http://dcxy\-customer\-app\.dcrym\.com/customerAccount/queryAccount requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/dcxy/dcxy.js

#txzxg
# http-request https:\/\/zxg\.txfund\.com\/xj\/fcgi\-bin\/xj\_config\_object\.fcgi requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/dcxy/txzxg.js
# http-response https:\/\/zxg\.txfund\.com\/xj\/fcgi\-bin\/xj\_config\_object\.fcgi requires-body=1,max-size=0,script-path=https://gitee.com/Nell3582/Nell9382/raw/master/dcxy/txzxg.js

