# -*- coding: utf-8 -*-
import dateJ

dateS = dateJ.MA

benjin = [10000]
pre = 60
fudong = []
half = []
halfB = []
kui = []
xishu = 0.5
for i in range(0,len(dateS)-3,1):
    half.append(round((float(dateS[i][1])+float(dateS[i + 1][1]))/2, 1))
    A = round(float(dateS[i][1]), 1)
    H1 = round((float(dateS[i][1])+float(dateS[i + 1][1]))*xishu, 1)
    B = round(float(dateS[i + 1][1]), 1)
    H2 = round((float(dateS[i + 1][1])+float(dateS[i + 2][1]))*xishu, 1)
    C = round(float(dateS[i + 2][1]), 1)
    D = round(float(dateS[i + 3][1]), 1)


    if i == 0 : # 第一次先取判断值half
        if A > B and H1 > C > D:
            pass
        if A > B and H2 > C < D:
            pass
        if A > B and D > H2 > C:
            print('C-D 反相,盈利 D-H2', dateS[i + 1][0], '-', dateS[i + 3][0])
            fudong.append(round((D - H2) * pre, 1))
            print('一次触发，盈利入浮动:', round(fudong[-1], 0))
            print('本金',benjin[-1])
            print('--------')


    if i != 0 :
        if A > B and H2 > C > D:
            print('B-D 单向', dateS[i + 1][0], '-', dateS[i + 3][0])
            fudong.append(round((B - D) * pre, 1))
            print('fudong', round(fudong[-1], 0))
            print('本金',benjin[-1])
            print('--------')
        if A > B and H2 > C < D:
            pass
        if A > B and D > H2 > C:
            print('C-D 反相,盈利 D-H2', dateS[i + 1][0], '-', dateS[i + 3][0])
            fudong.append(round((D - H2) * pre, 1))
            print('一次触发，盈利入浮动:', round(fudong[-1], 0))
            print('本金',benjin[-1])
            print('--------')

#quchuxiamian
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
        #
        # if A > B and H > C:
        #     pass
        #     # if qian yi H > A
        #     # print('C-B 反相', dateS[i + 1][0], '-', dateS[i + 2][0])
        #     # fudong.append(round((B - C) * pre, 1))
        #     # print('先亏损', round(fudong[-1], 0))
        #     # benjin.append(benjin[-1] + round((B - C) * pre, 1))
        #     # print('本金变化:',benjin[-1])
        #     # fudong.append(round((H - C) * pre, 1))
        #     # print('H-C 反相做空',dateS[i][0],'-',dateS[i + 2][0])
        #     # print('盈利',round(fudong[-1],0))
        #     # print('H:',H,'-','C',C)
        #     # print(dateS[i + 2][0],'点数:',round(H - C,1))
        #     # benjin.append(round(benjin[-1]+(H - C)*pre,1))
        #     # print('本金',benjin[-1])
        #     # print('--------')
        #
        # if A > B and H < C:
        #     print('C-H 反相', dateS[i + 1][0], '-', dateS[i + 2][0])
        #     fudong.append(round((B - H) * pre, 1))
        #     print('先亏损', round(fudong[-1], 0))
        #     benjin.append(benjin[-1] + round((B - H) * pre, 1))
        #     print('本金变化:', benjin[-1])
        #     fudong.append(round((C - H) * pre, 1))
        #     print('C-H 反相做空', dateS[i][0], '-', dateS[i + 2][0])
        #     print('盈利', round(fudong[-1], 0))
        #     print('H:', H, '-', 'C', C)
        #     print(dateS[i + 2][0], '点数:', round(C - H, 1))
        #     benjin.append(round(benjin[-1] + (C - H) * pre, 1))
        #     print('本金', benjin[-1])
        #     print('--------')


    # if A > B > C:
    #     benjin.append(round(benjin[-1]+(A - C)*pre,1))
    #     fudong.append(round((A - C)*pre,1))
    #     # halfB.append()
    #     print('策略（1）做空: A > B > C')
    #     print('盈利', fudong[-1])
    #     print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
    #     print('----------')
    #     print('')
    #
    # if A > B < C and half[-1] > C:
    #     benjin.append(round(benjin[-1]+(A - C)*pre,1))
    #     fudong.append(round((A - C)*pre,1))
    #     kui.append(round((B - C) * pre, 1))
    #     print('策略（2）做空: A > B < C and half > C')
    #     print('盈利', fudong[-1])
    #     print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
    #     print('----------')
    #     print('')
    #
    # if A > B < C and half[-1] < C:
    #     benjin.append(round(benjin[-1]+((A - half[-1])+(C-half[-1]))*pre,1))
    #     fudong.append(round(((A - half[-1])+(C-half[-1]))*pre,1))
    #     kui.append(round((B - half[-1]) * pre, 1))
    #     print('策略（3）反转做多: A > B < C and half < C')
    #     print('盈利', fudong[-1])
    #     print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
    #     print('----------')
    #     print('')
    #
    # if A < B < C:
    #     benjin.append(round(benjin[-1]+(C - A)*pre,1))
    #     fudong.append(round((C - A)*pre,1))
    #     kui.append(round((C - B) * pre, 1))
    #     print('half-1',half[-1])
    #     print('half-2',half[-2])
    #     print('策略（4）做多: A < B < C')
    #     print('盈利', fudong[-1])
    #     print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
    #     print('----------')
    #     print('')
    #
    # if A < B > C and half[-1] < C:
    #     benjin.append(round((benjin[-1]+(C -A)*pre),1))
    #     fudong.append(round((C - A)*pre,1))
    #     kui.append(round((C - A) * pre, 1))
    #     print('策略（5）做多: A < B > C and half[-1] < C')
    #     print('亏损',kui[-1])
    #     print('盈利', fudong[-1])
    #     print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
    #     print('----------')
    #     print('')
    #
    # if A < B > C and half[-1] > C:
    #     benjin.append(round(benjin[-1]+((half[-1] - A)+(half[-1] - C))*pre,1))
    #     fudong.append(round(((half[-1] - A)+(half[-1] - C))*pre,1))
    #     kui.append(round((half[-1] - B) * pre, 1))
    #     print('策略（6）反转做空: A < B > C and half[-1] > C')
    #     print('亏损', kui[-1])
    #     print('盈利', fudong[-1])
    #     print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
    #     print('----------')
    #     print('')

print('本金',benjin)
print('浮动',fudong)
# print('kui',kui)
# print(min(kui))
