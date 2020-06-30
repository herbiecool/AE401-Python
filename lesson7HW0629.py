# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:49:55 2020

@author: redno
"""
import random
name=['小明','小方','小志']
verb=['飛到','看到','走到']
noun=['日本。','綠島。','美國。']

for i in range(10):

    a=random.sample(name,1)
    b=random.sample(verb,1)
    c=random.sample(noun,1)
    
    str_a="".join(a)
    str_b="".join(b)
    str_c="".join(c)

    print('句子:',str_a+str_b+str_c)





