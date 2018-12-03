# -*- coding: utf-8 -*-、
# time        preclose	high	low	   match	open	volume
# 2013/10/28	1113.6 	1118.7 	1101.6 	1111.7 	1118.7 	1988130
#  0            1        2        3       4       5       6
#  策略-01 做多策略测试  在双周阴线时出现阳线买入 区分周线收盘价和周线最高价2种 再细分日周止损

import date,random
JM0 = date.JM0WK
fund = 15000
riskgold = fund*0.33 #ketiaozhen
print('riskgold',riskgold,'元')
onepoint = 60
fluctuation = []
signaldaynub = []
xishu = 0.5
for i in range(len(JM0)-1): #在双周阴线时出现阳线买入
    if float(JM0[i][4]) < float(JM0[i][5]) and float(JM0[i+1][4]) < float(JM0[i+1][5]) and \
            float(JM0[i+2][2]) > (float(JM0[i][2]) + float(JM0[i+1][4]))*xishu :
        signaldaynub.append(i)
print('signaldaynub',signaldaynub)

startday = random.choice(signaldaynub)
print('随机抽取条件日 startday',startday)
buyday = JM0[startday][0]
buyprice = random.randint(float(JM0[startday][3]),float(JM0[startday][2]))
print('buyday',buyday)
print('buyprice',buyprice,'点')

for i in range(startday,len(JM0)):#
    # if JM0[startday][4]

        fluctuation.append((float(JM0[i][4]) - buyprice) * onepoint) #zuixin fuyin fukui
        print('Running',JM0[i][0],'fluctuation:',riskgold + float(fluctuation[-1]))
        if (fluctuation[-1] + riskgold) < 0: # baocang
            print('OUT')







