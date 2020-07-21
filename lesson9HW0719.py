# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:48:07 2020

@author: redno
"""


import os.path

d = {}

def Menu():
    print('=>')
    print('1. 建立辭彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')

if not os.path.isfile('a.txt'):
    fo = open('a.txt', 'w')
    print('new file')
else:
    fo = open('a.txt', 'r')
    print('old file')

for row in fo.readlines():
    data = row.split(':')

    k = data[0]
    v = data[1]
    v = v.strip()

    d[k]=v
print(d)    
fo.close()

while True:
    Menu()

    sel = input('請輸入欲執行選項: ')

    if sel=='1':
        while True:
            voc = input('輸入新單字(按0停止輸入): ')
            if voc == '0':
                break
            if voc not in d:
                m = input('輸入中文解釋: ')
                d[voc] = m
            else:
                print('單字已經存在')
        print(d)
        if not os.path.isfile('a.txt'):
            fo = open('a.txt', 'w')
        else:
            fo = open('a.txt', 'w')
        for k,v in d.items():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('\n')
        fo.close()
        
    elif sel=='2':
        if not os.path.isfile('a.txt'):
            print('目前字典是空的!!!')
        else:
            fo = open('a.txt', 'r')
            foc = fo.read()
            print(foc)
            for row in fo.readlines():
                data = row.split(':')
                
    elif sel=='3': 
        voc = input('輸入要查詢的英文單字: ')
        if voc in d: 
            print(d[voc])
        else:
            print('我的字典沒有這個單字')
            
    elif sel=='4': 
        got=False
        ch = input('輸入要查詢的中文: ')
        for k,v in d.items():
            if ch==v:
                print(ch,'的英文是',k)
                got=True
        if not got:
            print('抱歉，查不到!')
                                      
    elif sel=='5':
        score=0
        print('The total score is', len(d), 'points')
        for k, v in d.items():
            print(v,':')
            ans = input()
            if ans == k:
                score += 1
                print('correct! you got', score, 'points now')
            else:
                print('wrong! you got', score, 'points now')
                
    elif sel=='6':
        break
    else:
        print('輸入錯誤，請重新輸入!')