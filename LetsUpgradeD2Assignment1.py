# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:32:49 2021

@author: Gourav
"""


import matplotlib.pyplot as plt
x1=[2,3,4,5,6,7,9]
y1=[4,7,2,6,7,8,3]
x2=[2,4,6,8,10]
y2=[5,6,2,6,2]
plt.bar(x1,y1,label="x-y variation")
plt.bar(x2,y2,color="g",label="x2-y2")
plt.title("bar graph")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()
plt.show()
