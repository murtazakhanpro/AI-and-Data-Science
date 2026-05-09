#### print("Welcome To the Bank Of Pakistan:")

name = input("Enter Your Name: ")
 # Pin System
pin = int(input("Enter Your 4 Digit Password:"))
if pin!= "7500":
    print("Acces Denied")
    # print(''' 1) Balance Inqueiry
    #          2) Cash Deposit
     #         3) Cash Withdraw ''')
#else:
balance = 52000

amount = int(input("Enter withdraw amount: "))

if amount > balance:
    print("Insufficient Funds")
else:
    remaining_bal = balance - amount
    
    print(f"Hello {name}, your current balance is {remaining_bal}")

    deposit = input("For Deposit Press (y) For Exit Press (n): ")

    if deposit == "y":
        deposit_amount = int(input("Please Enter Your Amount: "))
        remaining_bal = remaining_bal + deposit_amount
        print(f"Hello {name}, your updated balance is {remaining_bal}")
    else:
        print("Thanks For Using This ATM")

