# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:00 2020

@author: Herbie Chu
"""

import random
a=random.randint(1,20)
counter=1
while True:        
    if counter>5:
     break
    else:   
     print('input : ',str(counter),'times.')
     
    counter=counter+1
    
    guess=int(input('guess1~20:'))
    if guess==a:
        print('bingo!')        
        break
    else:
        print('wrong!')
        if guess>a:
            print('小一點')
        else:
            print('大一點')
            
     
        
    

    