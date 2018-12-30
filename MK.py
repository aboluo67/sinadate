# -*- coding: utf-8 -*-
# ["2016/1/4","567","570","554","555"],
import json,dateD_OR

JM0 = dateD_OR.JM0
clean1 = [] #date
clean2 = [] #op
clean3 = [] #top
clean4 = [] #low
clean5 = [] #c


print(len(JM0))

for i in range(len(JM0)-1):

    clean3.append(JM0[i][2])
    # print(clean3)
    clean4.append(JM0[i][3])

print(JM0[0][0],JM0[0][1],max(clean3),min(clean4),JM0[-1][4])