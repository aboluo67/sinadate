# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# x=np.linspace(0,10,100)
# y=np.sin(x)
# y1=np.cos(x)
# plt.figure(figsize=(8,4)) #整个现实图（框架）的大小
# plt.plot(x,y,'r-o',label="$sin(x)$",linewidth=1)
# plt.plot(x,y1,'b-o',label="$cose(x)$",linewidth=1)
# plt.xlabel('Time(s)')
# plt.ylabel("Volt")
# plt.title("Python chart")
# plt.show()


plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()