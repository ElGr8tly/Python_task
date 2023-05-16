import os
from time import sleep
#####################################################################
arrow_lenght=  20
space_down  =  5
space_right =  int(arrow_lenght/2)

#####################################################################
def Up_ARROW():
   for x in range(0,space_down):
       print("")
   for row in range(1,arrow_lenght,1):
   
       for j in range(0,space_right):
            print(" ",end='')
       if ( row <  int(arrow_lenght/2)):
         for i in range(row,int(arrow_lenght/2)):
           print(" ",end='')
		   
         for star in range(0,(2*row-1)):
           print("*",end='')

       else :
         for i in range(1,int(arrow_lenght/2)):
           print(" ",end='')
         print("*",end='')
       print("")

#####################################################################
def Right_Arow():
    for i in range(0,space_down+int(arrow_lenght/2)):
        print('')
    for row in range(1,arrow_lenght):
        for j in range(0,space_right):
          print(" ",end='')
        for j in range(1,int(arrow_lenght/2)):
          print(" ",end='')
        if row <= int(arrow_lenght/2):
            r = row
        elif row > int(arrow_lenght/2):
            r = r-1 
        for space in range(int(arrow_lenght/2)+r):
          if (row == int(arrow_lenght/2)): 
           print("*",end='')
          elif(space <=int(arrow_lenght/2)) :
           print(" ",end='')
          elif (space>int(arrow_lenght/2)):
           print("*",end='')
        print("")
#####################################################################
def Down_Arow():
    for i in range(0,space_down+arrow_lenght):
        print('')
    for row in range(1,arrow_lenght):
        for j in range(0,space_right):
          print(" ",end='')
        if row <= int(arrow_lenght/2):
            for j in range(0,int(arrow_lenght/2)):
                print(" ",end='')
            print("*",end='')
        elif row > int(arrow_lenght/2):
            rang = 1+row - int(arrow_lenght/2)
            for space in range(rang):
                print(" ",end='')
            for star in range(arrow_lenght+1 - 2*rang):
                print("*",end='')
        print("")

#####################################################################
def Left_Arrow():
    for i in range(0,space_down+int(arrow_lenght/2)):
        print('')
    for row in range(1,arrow_lenght):
        for j in range(0,space_right-int(arrow_lenght/2)):
          print(" ",end='')
        if row <= int(arrow_lenght/2):
            r = row
        elif row > int(arrow_lenght/2):
            r = r-1 
        if row == int(arrow_lenght/2):
            for j in range(1,arrow_lenght):
               print("*",end='')
        else :
            for j in range(0,int(arrow_lenght/2)-r):
               print(" ",end='')
            for j in range(1,r):
               print("*",end='')
        print("")
#####################################################################
delay = 1
while True:
    os.system('cls')
    Up_ARROW()
    sleep(delay)
    os.system('cls')
    Right_Arow()
    sleep(delay)
    os.system('cls')
    Down_Arow()
    sleep(delay)
    os.system('cls')
    Left_Arrow()
    sleep(delay)
    space_right += 10
