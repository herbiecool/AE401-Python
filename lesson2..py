# -*- coding: utf-8 -*-
"""
Created on Fri May 9 16:02:24 2020

@author: Herbie Chu
"""

import random
a=random.randint(1,20)
counter=1
while True:    
    if counter>5:
     break      
    guess=int(input('guess1~20:'))
    if guess==a:
        print('bingo!')
        counter=counter+1
        print(str(counter-1))
        break
    else:
        print('wrong!')
        if guess>a:
            print('小一點')
        else:
            print('大一點')
    counter=counter+1
    print(str(counter-1))

    