# -*- coding: utf-8 -*-
# time        preclose	high	low	   match	open	volume
# 2013/10/28	1113.6 	1118.7 	1101.6 	1111.7 	1118.7 	1988130
#  0            1        2        3       4       5       6
# 大阳阴线 + 区间内震荡 （i的H，L）

import date

JM0 = date.JM0
# JM0 = date.JM0WK

print(JM0[0])
print(JM0[0][5])
print(JM0[10])

for i in range(len(JM0)-3):
    if abs(float(JM0[i][4])-float(JM0[i][5])) > ((abs(float(JM0[i+1][4])-float(JM0[i+1][5])))+\
            abs(float(JM0[i+2][4])-float(JM0[i+2][5]))+abs(float(JM0[i+3][4])-float(JM0[i+3][5])))/3*1.05:#3tian  1.05xishu
        print(JM0[i][0])