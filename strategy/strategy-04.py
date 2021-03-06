# -*- coding: utf-8 -*-

dateS = [
["2013/3/22","1241.97"],
["2013/4/1","1140.77"],
["2013/5/2","1100.52"],
["2013/6/3","1028.43"],
["2013/7/1","1052.69"],
["2013/8/1","1139.01"],
["2013/9/2","1148.36"],
["2013/10/8","1101.63"],
["2013/11/1","1103.24"],
["2013/12/2","1010.27"],
["2014/1/2","938.44"],
["2014/2/7","923.51"],
["2014/3/3","834.51"],
["2014/4/1","823.75"],
["2014/5/5","826.29"],
["2014/6/3","812.28"],
["2014/7/1","772.63"],
["2014/8/1","794.83"],
["2014/9/1","780"],
["2014/10/8","763.8"],
["2014/11/3","763.9"],
["2014/12/1","744.24"],
["2015/1/5","728.12"],
["2015/2/2","728.09"],
["2015/3/2","690.11"],
["2015/4/1","671.33"],
["2015/5/4","688.51"],
["2015/6/1","677.84"],
["2015/7/1","614.27"],
["2015/8/3","567.79"],
["2015/9/1","570.85"],
["2015/10/8","553.15"],
["2015/11/2","536.24"],
["2015/12/1","566.27"],
["2016/1/4","553.07"],
["2016/2/1","608.94"],
["2016/3/1","634.28"],
["2016/4/1","768.19"],
["2016/5/3","680.37"],
["2016/6/1","725.29"],
["2016/7/1","769.23"],
["2016/8/1","853.77"],
["2016/9/1","1004.52"],
["2016/10/10","1287.5"],
["2016/11/1","1405.78"],
["2016/12/1","1183.96"],
["2017/1/3","1248.42"],
["2017/2/3","1241.74"],
["2017/3/1","1249.15"],
["2017/4/5","1129.03"],
["2017/5/2","947.38"],
["2017/6/1","1116.28"],
["2017/7/3","1319.43"],
["2017/8/1","1413.35"],
["2017/9/1","1130.73"],
["2017/10/9","1068.94"],
["2017/11/1","1374.45"],
["2017/12/1","1312.31"],
["2018/1/2","1292.39"],
["2018/2/1","1405.62"],
["2018/3/1","1261.6"],
["2018/4/2","1156.78"],
["2018/5/2","1238.09"],
["2018/6/1","1198.93"],
["2018/7/2","1202.77"],
["2018/8/2","1250.8"],
["2018/9/3","1267.58"],
["2018/10/8","1384.23"],
["2018/11/1","1272.68"],
["2018/12/3","1322.78"]]

benjin = [10000]
pre = 60
fudong = []
half = []
halfB = []
kui = []
for i in range(0,len(dateS)-2,2):
    half.append((float(dateS[i][1]) + float(dateS[i + 1][1])) / 2)
    halfB.append((float(dateS[i + 1][1]) + float(dateS[i + 2][1])) / 2)
    A = round(float(dateS[i][1]),1)
    B = round(float(dateS[i + 1][1]),1)
    C = round(float(dateS[i + 2][1]),1)
    print('half',half[-1])
    print('A',A,'B',B,'C',C)

    if A > B > C:
        benjin.append(round(benjin[-1]+(A - C)*pre,1))
        fudong.append(round((A - C)*pre,1))
        # halfB.append()
        print('策略（1）做空: A > B > C')
        print('盈利', fudong[-1])
        print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
        print('----------')
        print('')

    if A > B < C and half[-1] > C:
        benjin.append(round(benjin[-1]+(A - C)*pre,1))
        fudong.append(round((A - C)*pre,1))
        kui.append(round((B - C) * pre, 1))
        print('策略（2）做空: A > B < C and half > C')
        print('盈利', fudong[-1])
        print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
        print('----------')
        print('')

    if A > B < C and half[-1] < C:
        benjin.append(round(benjin[-1]+((A - half[-1])+(C-half[-1]))*pre,1))
        fudong.append(round(((A - half[-1])+(C-half[-1]))*pre,1))
        kui.append(round((B - half[-1]) * pre, 1))
        print('策略（3）反转做多: A > B < C and half < C')
        print('盈利', fudong[-1])
        print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
        print('----------')
        print('')

    if A < B < C:
        benjin.append(round(benjin[-1]+(C - A)*pre,1))
        fudong.append(round((C - A)*pre,1))
        kui.append(round((C - B) * pre, 1))
        print('half-1',half[-1])
        print('half-2',half[-2])
        print('策略（4）做多: A < B < C')
        print('盈利', fudong[-1])
        print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
        print('----------')
        print('')

    if A < B > C and half[-1] < C:
        benjin.append(round((benjin[-1]+(C -A)*pre),1))
        fudong.append(round((C - A)*pre,1))
        kui.append(round((C - A) * pre, 1))
        print('策略（5）做多: A < B > C and half[-1] < C')
        print('亏损',kui[-1])
        print('盈利', fudong[-1])
        print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
        print('----------')
        print('')

    if A < B > C and half[-1] > C:
        benjin.append(round(benjin[-1]+((half[-1] - A)+(half[-1] - C))*pre,1))
        fudong.append(round(((half[-1] - A)+(half[-1] - C))*pre,1))
        kui.append(round((half[-1] - B) * pre, 1))
        print('策略（6）反转做空: A < B > C and half[-1] > C')
        print('亏损', kui[-1])
        print('盈利', fudong[-1])
        print(dateS[i][0], '-', dateS[i + 1][0], '-', dateS[i + 2][0],benjin[-1])
        print('----------')
        print('')

print('本金',benjin)
print('浮动',fudong)
print('kui',kui)
print(min(kui))
