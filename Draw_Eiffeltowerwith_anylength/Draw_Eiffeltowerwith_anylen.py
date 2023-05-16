offset = 10
loop = 20
len=20
for y in range (len):
    r=0 
    for x in range ((len+1)*2):
        if ((y**2+r**2)>=len**2) and (x<len) :
            print("*",end="")
            r+=1
        elif(x<len):
            print(" ",end="")
            r+=1

        elif ((y**2+r**2)>=len**2) and (x>=len):
            print("*",end="")
            r-=1
        elif(x>=len) :
            print(" ",end="")
            r-=1
    print()
