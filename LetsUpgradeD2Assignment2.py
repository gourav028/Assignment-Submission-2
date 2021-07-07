# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:26:33 2021

@author: Gourav
"""

#Create a Datframe with 10 rows on random numbers and 4 columns
import pandas as pd
import random
import matplotlib.pyplot as plt
res1=[random.randrange(1,10) for i in range(7)]
res2=[random.randrange(1,10) for i in range(7)]
res3=[random.randrange(1,10) for i in range(7)]
res4=[random.randrange(1,10) for i in range(7)]
data={"A":res1,"B":res2,"C":res3,"D":res4}
df = pd.DataFrame(data)
print(df)
df.plot(kind="bar")
