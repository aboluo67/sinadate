# -*- coding: utf-8 -*-
# ["2013-03-22","1280.000","1304.000","1257.000","1267.000","845512"],

import dateD

JM = dateD.JM0

for i in range(len(JM)-1):
    if abs(float(JM[i][4]) - float(JM[i +1][1])) > 30:
        print(JM[i][0],float(JM[i][4]) - float(JM[i +1][1]))