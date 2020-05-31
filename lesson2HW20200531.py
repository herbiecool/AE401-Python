# -*- coding: utf-8 -*-
"""
Created on Fri May 9 16:02:24 2020

@author: Herbie Chu
"""

MATHscore=input('輸入數學成績:')
ENGscore=input('輸入英文成績:')

Math_float=float(MATHscore)
Eng_float=float(ENGscore)

if (0<=Eng_float<=100) & (0<=Math_float<=100):
    if (Eng_float>90) & (Math_float>90):
        print('good')
    elif (Eng_float>=60) & (Math_float>=90):
        print('再加油')
    elif (Eng_float>=90) & (Math_float>=60):
        print('再加油')    
    elif (Eng_float<60) & (Math_float<60):
        print('不及格')
    
else:
    print('please input number between 0 ~ 100')
            


           
                    