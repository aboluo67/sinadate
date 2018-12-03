# -*- coding: utf-8 -*-
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
        checklow.append(JM0[xday+i-1][3])
        checkhigh.append(JM0[xday+i-1][2])

    if float(max(checkhigh)) - xprice >0: #15tiannei you dayu xprice
        print('PLUS',round(float(max(checkhigh)) - xprice,2))
        PLUSdate.append(round(float(max(checkhigh)) - xprice,2))
    else:
        print('NEG',round(float(min(checklow)) - xprice,2))
        NEGdate.append(round(float(min(checklow)) - xprice,2))

print(PLUSdate)
print(NEGdate)


