# -*- coding: utf-8 -*-、
# time        preclose	high	low	   match	open	volume
# 2013/10/28	1113.6 	1118.7 	1101.6 	1111.7 	1118.7 	1988130
#  0            1        2        3       4       5       6
import date,random
JM0 = date.JM0WK
PLUSdate = []
NEGdate = []
for i in range(0,50):
    checkopen = []
    checkhigh = []
    checklow = []
    checkclose = []
    PLUS = 0
    NEG = 0
    xday = random.randint(1,len(JM0))
    xprice = random.uniform(float(JM0[xday][3]),float(JM0[xday][2]))
    xprice = round(xprice,2)
    print('xday',xday,JM0[xday][0],xprice)

    for i in range(0,16):
        checklow.append(JM0[xday+i-2][3])
        checkhigh.append(JM0[xday+i-2][2])

    if float(max(checkhigh)) - xprice >0: #15tiannei you dayu xprice
        print('PLUS',round(float(max(checkhigh)) - xprice,2))
        PLUSdate.append(round(float(max(checkhigh)) - xprice,2))
    else:
        print('NEG',round(float(min(checklow)) - xprice,2))
        NEGdate.append(round(float(min(checklow)) - xprice,2))

print(PLUSdate)
print(NEGdate)


# -*- coding: utf-8 -*-、
# time        preclose	high	low	   match	open	volume
# 2013/10/28	1113.6 	1118.7 	1101.6 	1111.7 	1118.7 	1988130
#  0            1        2        3       4       5       6
#  策略-01  在双周阴线时出现阳线买入 区分周线收盘价和周线最高价2种 再细分日周止损

import date,random
JM0 = date.JM0WK
fund = 15000
riskgold = fund*0.33 #ketiaozhen
print('riskgold',riskgold,'元')
onepoint = 60
fluctuation = []
startday = random.randint(0,len(JM0))
print('startday',startday)
buyday = JM0[startday][0]
buyprice = random.randint(float(JM0[startday][3]),float(JM0[startday][2]))
print('buyday',buyday)
print('buyprice',buyprice,'点')
for i in range(startday,len(JM0)):# xuanzezuoduo
    fluctuation.append((float(JM0[i][4]) - buyprice) * onepoint) #zuixin fuyin fukui
    print('Running',JM0[i][0],'fluctuation:',riskgold + float(fluctuation[-1]))
    if (fluctuation[-1] + riskgold) < 0: # baocang
        print('OUT')















































