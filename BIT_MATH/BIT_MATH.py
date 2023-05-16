reg1 = 0x5555
reg2 = 0xFFFF
reg3 = 0x0000
Reg = [reg1 , reg2 ,reg3]

def set_bit (reg,pos):
   global Reg
   Reg[reg] |= (1<<pos)
   
def clr_bit (reg,pos):
   global Reg
   Reg[reg] &= ~(1<<pos)
   
def tog_bit (reg,pos):
   global Reg
   Reg[reg] ^= (1<<pos)
   
print("********************")
print(Reg[Reg.index(reg1)])
set_bit(Reg.index(reg1),1)
print(Reg[Reg.index(reg1)])
print("********************")
print(Reg[Reg.index(reg2)])
clr_bit(Reg.index(reg2),1)
print(Reg[Reg.index(reg2)])
print("********************")
print(Reg[Reg.index(reg3)])
tog_bit(Reg.index(reg3),1)
print(Reg[Reg.index(reg3)])
print("********************")