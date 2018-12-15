# -*- coding: utf-8 -*-
# 手动完成第一周K线（非实时）
# 从当天倒推周K线（实时）

import json,dateD

# import datetime
#
# print(datetime.datetime.now())
# print(datetime.datetime.now().weekday())
# # 0 tian 1 一
#
# # 非实时
# from urllib import request
# url='http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=AP0'
# req = request.Request(url)
# res = request.urlopen(req)
# res = res.read()
# res = res.decode(encoding='utf-8')
# print(type(res))
# # 转换成list
# JM0 = json.loads(res)


step = 5
P1JM0 = [dateD.JM0[i:i+step] for i in range(0,len(dateD.JM0),step)] # 每五个归入一个list


clean1 = [] #date
clean2 = [] #op
clean3 = [] #top
clean4 = [] #low
clean5 = [] #c
each_wkdate = []
all_wkdate = []

for i in range(len(P1JM0)):  # 大集合里的5组数量
    try:
        each_wkdate = []
        # print(P1JM0[i])
        # print(len(P1JM0))
        # print(P1JM0[i][0][0])
        for ii in range(5):
            clean1.append(P1JM0[i][ii][0])
            clean2.append(P1JM0[i][ii][1])
            clean3.append(P1JM0[i][ii][2])
            clean4.append(P1JM0[i][ii][3])
            clean5.append(P1JM0[i][ii][4])

        each_wkdate.append(clean1[-1])
        # print('clean1')
        # print(clean1)
        each_wkdate.append(clean2[0])
        each_wkdate.append(max(clean3))
        each_wkdate.append(min(clean4))
        each_wkdate.append(clean5[-1])
        clean1 = []  # date
        clean2 = []  # op
        clean3 = []  # top
        clean4 = []  # low
        clean5 = []  # c
        # each_wkdate = []
        all_wkdate.append(each_wkdate)
    except:
        pass
# print(each_wkdate)
# print(all_wkdate)


for i in all_wkdate:
    print(i)