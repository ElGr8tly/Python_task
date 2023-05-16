
import goto 
import math
import os 
from time import sleep


def Welcome_Seintefic():
    print("*********************************")
    print("******Sientific Operations*******")
    print("*********************************")
    SimpleOperation="Operations : A + B  , A - B \n\t     A * B , A / B  "
    AlgebricOperation=[" SQR( A ) \n log( A ) \n A^B \n A^2  \nEnter Yor Operations \"Please dont forget spaces \": "]
    print(SimpleOperation)
    print(AlgebricOperation)

def Welcome_programmer():
    print("*********************************")
    print("******Programmer Operations******")
    print("*********************************")
    ProgrmerOperation = "Targets :\n0-Binary \n1-Octal \n2-decimal \n3-hex \nEnter the conversion target : "
    print(ProgrmerOperation)



def SQR_ROOT():
    print("************   (square root)    *************")
    op1=int(input("enter the value "))
    print("the square root is ",math.sqrt(op1))


def LOG():
    print("************   (log)    *************")
    op1=int(input("enter the value "))
    print("the log is ",math.log(op1))


def Sientific_calcualtor():

    while True :

        Welcome_Seintefic()
        result = 0 
        op=input()
        sleep(0.5)
        os.system('cls')
        print("Anwser : ")
        print(op, "  : ",end='')
        op =op.split()  #A + B 
        if op[1]   == "+": 
           result = float(float(op[0])+float(op[2]))
           break
        elif op[1] == "-":
           result = float(float(op[0])-float(op[2]))
           break
        elif op[1] == "*":
           result = float(float(op[0])*float(op[2]))
           break
        elif op[1] == "/":
           result = float(float(op[0])/float(op[2]))
           break
        elif op[1] == "^":
           result = float(float(op[0])**float(op[2])) 
           break
        elif op[0] == "SQR(":
           result=math.sqrt(float(op[1]))
           break
        elif op[0] == "log(":
           result=math.log(float(op[1]))    
           break
        else:
            print("wrong selection operation (must put space between elemnts )")
    print(result)

def Programer_calcualtor():

    while True :

        Welcome_programmer()
        selec = int(input())
        base = [2 , 8 , 10 , 16]
        w = ["A >> B \nA << B \nA + B \nA - B"]
        print(w)
        op=input("Enter Operation : ")
        sleep(0.5)
        os.system('cls')
        print(op ," ")
        op =op.split()
        if op[1]== "<<": 
            s=int(op[0],base[selec])
            for x in range(int(op[2],base[selec])) :
                s=s * (base[selec])
            break
        elif op[1]== ">>":
            s=int(int(op[0],base[selec])) 
            for x in range(int(op[2],base[selec])) :
                s=int(s/(base[selec]))
            break
        elif op[1]== "+": 
            s=int(op[0],base[selec]) + (int(op[2],base[selec]))
            break
        elif op[1]== "-": 
            s=int(op[0],base[selec]) - (int(op[2],base[selec]))
            break
        else :
            print("wrong selection operation ( must put space between elemnts )\n")

        
    print("Results : ")
    print("DEC : ",s)
    p=hex(s)
    print("HEX : ",p)
    p=oct(s)
    print("OCT : ",p)
    p=bin(s)
    print("BIN : ",p)
    
