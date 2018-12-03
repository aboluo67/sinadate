# -*- coding: utf-8 -*-

import date
JM0 = date.JM0WK
# time        preclose	high	low	   match	open	volume
# 2013/10/28	1113.6 	1118.7 	1101.6 	1111.7 	1118.7 	1988130
#  0            1        2        3       4       5       6
print('all:',len(JM0))
yin = 0
yang = 0
yinall = 0
yangall = 0
yinsy = 0 #上影
yangsy = 0
lianglianyin = 0
sanlianyin = 0
silianyin = 0
wulianyin = 0
lianglianyang = 0
sanlianyang = 0
silianyang = 0
wulianyang = 0


for i in range(len(JM0)-1):
    if (float(JM0[i][5]) - float(JM0[i][4])) > 0:
        yin += 1
        yinall += float(JM0[i][4]) - float(JM0[i][5])
        yinsy += float(JM0[i][5]) - float(JM0[i][2])
        # print(float(JM0[i][5]) - float(JM0[i][4]))
        # print('yinall',yinall)
    if (float(JM0[i][4]) - float(JM0[i][5])) >= 0:
        yang += 1
        yangall += float(JM0[i][4]) - float(JM0[i][5])
        yangsy += float(JM0[i][2]) - float(JM0[i][4])
        # print(float(JM0[i][4]) - float(JM0[i][5]))
        # print('yangall',yangall)
    if (float(JM0[i][4]) - float(JM0[i][5])) < 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) < 0 :
        lianglianyin += 1
        # print(JM0[i][0])
        # 2阴低于前收 排除跳空阴线
    if (float(JM0[i][4]) - float(JM0[i][5])) > 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) > 0 :
        lianglianyang += 1
        # print(JM0[i][0])

    if (float(JM0[i][4]) - float(JM0[i][5])) < 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) < 0 and \
       (float(JM0[i + 2][4]) - float(JM0[i + 1][4])) < 0:#3阴低于前收 排除跳空阴线
        sanlianyin += 1
    if (float(JM0[i][4]) - float(JM0[i][5])) > 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) > 0 and \
       (float(JM0[i + 2][4]) - float(JM0[i + 1][4])) > 0:#2liamyang
        sanlianyang += 1

    if (float(JM0[i][4]) - float(JM0[i][5])) < 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) < 0 and \
       (float(JM0[i + 2][4]) - float(JM0[i + 1][4])) < 0 and \
       (float(JM0[i + 3][4]) - float(JM0[i + 2][4])) < 0:#3阴低于前收 排除跳空阴线
        silianyin += 1
    if (float(JM0[i][4]) - float(JM0[i][5])) > 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) > 0 and \
       (float(JM0[i + 2][4]) - float(JM0[i + 1][4])) > 0 and \
       (float(JM0[i + 3][4]) - float(JM0[i + 2][4])) > 0:#3liamyang
        silianyang += 1

    if (float(JM0[i][4]) - float(JM0[i][5])) < 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) < 0 and \
       (float(JM0[i + 2][4]) - float(JM0[i + 1][4])) < 0 and \
       (float(JM0[i + 3][4]) - float(JM0[i + 2][4])) < 0 and \
       (float(JM0[i + 4][4]) - float(JM0[i + 3][4])) < 0:#4阴低于前收 排除跳空阴线
        wulianyin += 1
    if (float(JM0[i][4]) - float(JM0[i][5])) > 0 and \
       (float(JM0[i+1][4]) - float(JM0[i][4])) > 0 and \
       (float(JM0[i + 2][4]) - float(JM0[i + 1][4])) > 0 and \
       (float(JM0[i + 3][4]) - float(JM0[i + 2][4])) > 0 and \
       (float(JM0[i + 4][4]) - float(JM0[i + 3][4])) > 0:
        wulianyang += 1

print('阴',yin,'阳',yang)
print('---')
print('阴all',yinall,'阳all',yangall)
print('---')
print('阴sy',yinsy,'阳sy',yangsy)
print('---')
print('两连阴',lianglianyin,'%.1f%%' %(100*lianglianyin/len(JM0)))
print('---')
print('两连阳',lianglianyang,'%.1f%%' %(100*lianglianyang/len(JM0)))
print('---')
print('三连阴',sanlianyin,'%.1f%%' %(100*sanlianyin/len(JM0)))
print('---')
print('三连阳',sanlianyang,'%.1f%%' %(100*sanlianyang/len(JM0)))
print('---')
print('4连阴',silianyin,'%.1f%%' %(100*silianyin/len(JM0)))
print('---')
print('4连阳',silianyang,'%.1f%%' %(100*silianyang/len(JM0)))
print('---')
print('5连阴',wulianyin,'%.1f%%' %(100*wulianyin/len(JM0)))
print('---')
print('5连阳',wulianyang,'%.1f%%' %(100*wulianyang/len(JM0)))
