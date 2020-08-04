# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:47:57 2020

@author: redno
"""


def MultiplicationTable():
    a=int(input('輸入想乘到的地方:'))
    for i in range(a):
        for l in range(10):
            n=i*l
            print(i*l,n)
    
    
print(MultiplicationTable())    
    
    
    
    