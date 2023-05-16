import claculatorfunctions as c
import goto 
import math
import os 
from time import sleep

os.system("cls")
while True :
     
     s = '''*********************************
             Choose Your Calculator 
     
           1-  scientific calcualtor 
           2-  programmer calculator 

*********************************'''
     print(s)
     calc_type=int(input("enter the calculator type : "))
     #start if condition of select calculator
     
     # if the selection is scientific  
     if calc_type == 1:
         c.Sientific_calcualtor()
         sleep(5)
         os.system("cls")
     #if the selection is programer 
     elif calc_type == 2 :
         c.Programer_calcualtor() 
         sleep(5)
         os.system("cls")
             
     


 
    


#if the selection is non of list 
#else : 

