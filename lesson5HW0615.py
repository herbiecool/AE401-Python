# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:27:41 2020

@author: redno
"""
scores=[]

position=0

人數=input('有幾人?')

for i in range(int(人數)):
    
    a=str(input('名字?'))
    scores.insert(position,a)
    
    b=int(input('幾分?'))
    scores.insert(position+1,b)

    position = position + 2 

high=0

for i in scores:
    if type(i)==int:
        if i>int(high):
         high=i
         high_index=scores[scores.index(i)-1]
print('人名:',high_index)          
print('最高分:',high)

low=100

for i in scores:
    if type(i)==int:
        if i<int(low):
         low=i
         low_index=scores[scores.index(i)-1]
print('人名:',low_index)          
print('最低分:',low)            
            
total=0
for i in scores:
    
    if type(i)==int:
       total=total+i
        
print('平均:',total/int(人數))            
            
            
            
            
            