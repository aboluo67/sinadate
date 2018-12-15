# -*- coding: utf-8 -*-
# 201812091935
import dateJ

dateS = dateJ.MA

benjin = [10000]
pre = 60
fudong = []
H = []
celv = [] # 0:做空  1:做多
kui = []
for i in range(0,len(dateS)-3,1):
    H.append(round((float(dateS[i][1])+float(dateS[i + 1][1]))/2, 1))
    A = round(float(dateS[i][1]), 1)
    B = round(float(dateS[i + 1][1]), 1)
    H = round((float(dateS[i][1])+float(dateS[i + 1][1]))/2, 1)
    C = round(float(dateS[i + 2][1]), 1)


    if i == 0 : # 第一次先取判断值half
        if A < B and H > C:
            print('H-C 反相做空', dateS[i][0], '-', dateS[i + 2][0])
            fudong.append(round((H - C) * pre,1))
            print('盈利', round(fudong[-1], 0))
            print('H:', H, '-', 'C', C)
            print(dateS[i + 2][0], '点数:', round(H - C, 1))
            benjin.append(round(benjin[-1] + (H - C) * pre, 1))
            print('本金', benjin[-1])
            print('--------')
        if A < B and C > H:
            print('pass',dateS[i][0], '-', dateS[i + 2][0])
            pass

        if A > B and H > C:
            print('pass',dateS[i][0], '-', dateS[i + 2][0])
            print('本金',benjin[-1])
            print('--------')
            pass

        if A > B and H < C:
            print('C-H 反相做空', dateS[i][0], '-', dateS[i + 2][0])
            fudong.append(round((C - H) * pre,1))
            print('盈利', round(fudong[-1], 0))
            print('C', C, '-','H:', H )
            print(dateS[i + 2][0], '点数:', round(C - H, 1))
            benjin.append(round(benjin[-1] + (C - H) * pre, 1))
            print('本金', benjin[-1])
            print('--------')


    if i != 0 :
        if A < B and H > C:
            print('H-B 反相', dateS[i + 1][0], '-', dateS[i + 2][0])
            fudong.append(round((H - B) * pre, 1))
            print('先亏损', round(fudong[-1], 0))
            benjin.append(benjin[-1] + round((H - B) * pre, 1))
            print('本金变化:',benjin[-1])
            fudong.append(round((H - C) * pre, 1))
            print('H-C 反相做空',dateS[i][0],'-',dateS[i + 2][0])
            print('盈利',round(fudong[-1],0))
            print('H:',H,'-','C',C)
            print(dateS[i + 2][0],'点数:',round(H - C,1))
            benjin.append(round(benjin[-1]+(H - C)*pre,1))
            print('本金',benjin[-1])
            print('--------')

        if A < B and C > H: #可能是 C-A
            print('H-B 反相', dateS[i + 1][0], '-', dateS[i + 2][0])
            fudong.append(round((H - B) * pre, 1))
            print('先亏损', round(fudong[-1], 0))
            benjin.append(benjin[-1] + round((H - B) * pre, 1))
            print('本金变化:',benjin[-1])
            fudong.append(round((H - C) * pre, 1))
            print('H-C 反相做空',dateS[i][0],'-',dateS[i + 2][0])
            print('盈利',round(fudong[-1],0))
            print('H:',H,'-','C',C)
            print(dateS[i + 2][0],'点数:',round(H - C,1))
            benjin.append(round(benjin[-1]+(H - C)*pre,1))
            print('本金',benjin[-1])
            print('--------')

        if A > B and H > C:
            pass
            # if qian yi H > A
            # print('C-B 反相', dateS[i + 1][0], '-', dateS[i + 2][0])
            # fudong.append(round((B - C) * pre, 1))
            # print('先亏损', round(fudong[-1], 0))
            # benjin.append(benjin[-1] + round((B - C) * pre, 1))
            # print('本金变化:',benjin[-1])
            # fudong.append(round((H - C) * pre, 1))
            # print('H-C 反相做空',dateS[i][0],'-',dateS[i + 2][0])
            # print('盈利',round(fudong[-1],0))
            # print('H:',H,'-','C',C)
            # print(dateS[i + 2][0],'点数:',round(H - C,1))
            # benjin.append(round(benjin[-1]+(H - C)*pre,1))
            # print('本金',benjin[-1])
            # print('--------')

        if A > B and H < C:
            print('C-H 反相', dateS[i + 1][0], '-', dateS[i + 2][0])
            fudong.append(round((B - H) * pre, 1))
            print('先亏损', round(fudong[-1], 0))
            benjin.append(benjin[-1] + round((B - H) * pre, 1))
            print('本金变化:', benjin[-1])
            fudong.append(round((C - H) * pre, 1))
            print('C-H 反相做空', dateS[i][0], '-', dateS[i + 2][0])
            print('盈利', round(fudong[-1], 0))
            print('H:', H, '-', 'C', C)
            print(dateS[i + 2][0], '点数:', round(C - H, 1))
            benjin.append(round(benjin[-1] + (C - H) * pre, 1))
            print('本金', benjin[-1])
            print('--------')



print('本金',benjin)
print('浮动',fudong)
# print('kui',kui)
# print(min(kui))
