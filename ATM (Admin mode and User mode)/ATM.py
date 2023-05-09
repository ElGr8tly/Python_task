# PYTHON ATM PROGRAM BY PYTHONDEX
# Visit https://pythondex.com for more information

user = {
    'pin':    ['Admin1111','1234'],
    'balance':[0,1000],
	'name':   ["Admin : Mohamed Yehia","Ahmed Yehia"],
	'ID':     [0,1]
}

def balance_enquiry(i):
    print(f"Total balance {user['balance'][i]} Dollars")
    print('')

def widthdraw_cash(i):
    while True:
        amount = int(input("Enter the amount of money you want to widthdraw  or  if you want return back press '0': "))
        if amount > user['balance'][i]:
            print("You don't have sufficient balance to make this widthdraw ")
        elif amount == 0:
            print("You chose to back ")
            return False
        else:
            user['balance'][i] = user['balance'][i] - amount
            print(f"{amount} Dollars successfully widthdrawn your remaining balance is {user['balance'][i]} Dollars")
            print('')
            return False

def deposit_cash(i):
    amount = int(input("Enter the amount of money you want to deposit or  if you want return back press '0': "))
    if amount == 0:
            print("You chose to back ")
            return False
    else:
            user['balance'][i]  = user['balance'][i] + amount
            balance_enquiry(i)


while True:
 print('')
 print("Welcome to the Pythondex ATM")

 pin = input('Please Enter Your PIN: ')

 if pin == user['pin'][0]:
  is_quit = False
  print("Welcome ",user['name'][0]," in Admin Mode")
  while is_quit == False:

    print("what do you want to do")
    print(" Enter 1 to Add user \n Enter 2 Delete user \n Enter 3 to Quit Admin Mode")
	
    query = int(input("Enter the number corresponding to the activity you want to do: "))
    if query == 1:
        print("All users ids : ",user['ID'])
        idd = int(input("chose New ID : "))
        if idd in user['ID']:
          print("Repeated ID !")
        else :		
          user['ID'].append(idd)
          user['name'].append(input("Enter user Name : "))
          user['pin'].append(input("Enter user PIN : "))
          user['balance'].append(int(input("Enter user Balance : ")))
		
    elif query == 2:
        print("All users ids : ",user['ID'][1:])
        idd = int(input("chose ID : "))
        if idd in user['ID'][1:]:
           i = user['ID'].index(idd)
           del user['ID'][i]
           del user['name'][i]
           del user['pin'][i]
           del user['balance'][i]
		   
        else : 
           print("This ID not found !")
		   
    elif query == 3:
        is_quit = True
		
    else :
        print("Enter wirte Number !")

 elif pin in user['pin'][1:]:
        i = user['pin'].index(pin)
        print("Welcome ",user['name'][i],"in User Mode")
    
        print("what do you want to do")
        print(" Enter 1 to Widthdraw Cash \n Enter 2 for Deposit \n Enter 3 for Balance \n Enter 4 to Quit User Mode")

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if   query == 1:
            widthdraw_cash(i)
        elif query == 2:
            deposit_cash(i)
        elif query == 3 :
            balance_enquiry(i)
        elif query == 4:
            is_quit = True
        else:
            print("Please enter a correct value shown")
 else:
    print("Entered wrong pin")