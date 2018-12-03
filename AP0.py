# -*- coding: utf-8 -*-
import json,re

# 非实时
from urllib import request
url='http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=AP0'
req = request.Request(url)
res = request.urlopen(req)
res = res.read()
res = res.decode(encoding='utf-8')
print(type(res))
# 转换成list
res = json.loads(res)
print(type(res))
print(res[-1])

print('----')


# 实时
url='http://hq.sinajs.cn/list=AP0'
req = request.Request(url)
res = request.urlopen(req)
res = res.read()
res = str(res)
print(type(res))
p = r'\d\d*\.\d*'
nowprice =  re.compile(p)
print(nowprice.findall(res))
print(nowprice.findall(res)[6])
