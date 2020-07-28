# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:16:32 2020

@author: redno
"""


import os.path

while True:
    print('=>')
    print('1.輸入檔案')
    print('2.單字出現次數(範圍內)')
    print('3.替換單字')
    print('4.離開')

    sel=input('請輸入欲執行選項:')
    
    if sel=='1':        
        f=input('檔案名稱:')
        if os.path.isfile(f):
            print('有這個檔案')
        file=open(f,'r')
        a=file.read()
        file.close()
                
    elif sel=='2':
           a=open(f,'r')
           c=a.read()
           a.close()
           print(c)
           v=input('想查詢的單字?')
           s=int(input('從哪裡開始:'))
           f=int(input('從哪裡結束:'))
           print('出現次數:',c.count(v,s,f))
             
    elif sel=='3':
           o=input('輸入想替換的舊單字:')
           n=input('輸入想替換的新單字:')
           a=c.replace(o,n)
           f=input('檔案名稱:')
           file=open(f,'w')
           file.write(a)
           file.close()
 
    elif sel=='4':   
            break
    else:
        print('輸入錯誤，請重新輸入!')  
    
    
    
    
    
    
    


