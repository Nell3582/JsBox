import requests

import json

def getRemoteData():
    ctrl = True
    while (ctrl):
        url = "https://gitee.com/Nell3582/Nell9382/raw/master/Task/zqkd/setData.json"  # 等价下面的
        res = requests.get(url).text
        if '无法显示' not in res:
            ctrl = False
    return res

print(getRemoteData())


# def readData():
#     array = []  # 定义list用于保存账号信息
#     dic = {}
#     res = getRemoteData()
#     res = res.replace('\n','\r')
#     lst = res.split('\r')
#     print(lst)

#     try:
#         for line in lst:
#             # print(line)
#             nline = line.split(',')
#             tel = nline[0]
#             print(tel)
#             merge = nline[1]+"@"+nline[2]
#             dic[tel] = merge
#     except:
#         print('pass')
#     return dic

# dic = readData()
# f = '数据汇总.json'
# with open(f, 'w') as new_f:
#     json.dump(dic, new_f, indent=4)
#     print("add account ")