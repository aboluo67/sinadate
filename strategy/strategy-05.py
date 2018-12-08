# -*- coding: utf-8 -*-、
# time        preclose	high	low	   match	open	volume
# 2013/10/28	1113.6 	1118.7 	1101.6 	1111.7 	1118.7 	1988130
#  0            1        2        3       4       5       6
#["2014/2/28","10524.26","10524.26","10524.26","10524.26","10524.26","191708"],
#  策略-05 周线级别 塑料主连160108-160115 大阴线+次小阴长下引

import dateW

date = dateW.FG
No = 0

for i in range(len(date)-1):
    A = date[i]
    B = date[i + 1]

    if float(A[5]) > float(A[4]) and float(B[5]) > float(B[4]) : # 第二根回测阳线
        if (float(B[4]) - float(B[3]))/(float(B[5]) - float(B[4])) > 2:
            No += 1
            print(No,A[0])




