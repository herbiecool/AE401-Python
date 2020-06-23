# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:27:41 2020

@author: redno
"""

#變數
scores=[]
Number_Person=0
Global_Number_Person=0

#函數 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Output_Number_Person(Number_Person):   
    Number_Person = int(input('有幾人?'))
    return Number_Person

def High_score(scores):
    high=0

    for i in scores:
        if type(i)==int:
            if i>int(high):
                high=i
                high_index=scores[scores.index(i)-1]
    print('人名:',high_index)          
    print('最高分:',high,'分')
    return

def Low_score(scores):
    low=100

    for i in scores:
        if type(i)==int:
            if i<int(low):
             low=i
             low_index=scores[scores.index(i)-1]
    print('人名:',low_index)          
    print('最低分:',low,'分')            
    return

def Average_score(scores):        
    total=0
    for i in scores:
    
        if type(i)==int:
            total=total+i
           
        average_score = total//Global_Number_Person
    print('平均:',average_score,'分')
    return
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#主程式 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
Global_Number_Person=Output_Number_Person(Number_Person)

position=0
for i in range(int(Global_Number_Person)):
    
        Name=str(input('名字?'))
        scores.insert(position,Name)
    
        Score=int(input('幾分?'))
        scores.insert(position+1,Score)

        position = position + 2        


High_score(scores)
Low_score(scores)
Average_score(scores)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
            
            