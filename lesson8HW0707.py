# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:14:00 2020

@author: redno
"""

num=0
dict_Eng=0
dictionary=[]


while True:
    print('1.設定')
    print('2.英翻中')
    print('3.中翻英')
    print('4.學習成果')
    print('5.離開')
   
    sel=input('輸入執行選項:')
    
    if sel=='1':
       num=int(input('有幾個單字:'))
    
       position=0
       for i in range(num):
             Chi=str(input('中文:'))
             Eng=str(input('英文:'))
             
             dictionary.insert(position,Chi)                 
             dictionary.insert(position+1,Eng)
             
             position = position + 2
             
    elif sel=='2':
          input_Eng=input('輸入英文單字:')
         
          for i in range(len(dictionary)):                   
                   dict_word=dictionary[i]
                                                                
                   if input_Eng == dict_word:   #找到英文單字
                      Chi_dict_word=dictionary[i-1]              
                      print('該單字翻譯為:',Chi_dict_word)
                      
    elif sel=='3':
          input_Chi=input('輸入中文單字:')
         
          for i in range(len(dictionary)):                   
                   dict_word=dictionary[i]
                                                                
                   if input_Chi == dict_word:   #找到中文單字
                      Eng_dict_word=dictionary[i+1]              
                      print('該單字翻譯為:',Eng_dict_word)
              
    elif sel=='5':
          break        
              
    

             
 
    