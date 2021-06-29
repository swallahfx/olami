# atm
import getpass

acct_balance = 10000
print("You are welcome to pytBank ")
user_name = input("pls, input your user name: ")
card_num= input("pls, input your card number: ")

if (card_num[0] == 5 and len(card_num) == 16):                              
    user_pass = getpass.getpass("pls, input your password: ")
    print(len(user_pass) * '*')
    print("You are welcome to pytBank,  how much would you like to withdraw")
    withdraw_amt = int(input("withdrawal amount: "))
    if acct_balance >= withdraw_amt :                        
        print("withdrawl amount of ", withdraw_amt, "successful you have ",acct_balance - withdraw_amt, "left")
    else:
        (acct_balance < withdraw_amt)
        print("insufficient fund, go and make money")
elif (card_num[0] == 4) and (len(card_num) == 14):
    user_pass = getpass.getpass("pls, input your password: ")
    print(len(user_pass) * '*')
    print("You are welcome to pytBank,  how much would you like to withdraw")
    withdraw_amt = int(input("withdrawal amount: "))

    if (acct_balance >= withdraw_amt):                           
        print("withdrawl amount of ", withdraw_amt, "successful you have ",acct_balance-withdraw_amt, "left")
    else:
        (acct_balance < withdraw_amt)
        print("insufficient fund, go and make money")
elif (card_num[0] == 5 and len(card_num) == 19):
    user_pass = getpass.getpass("pls, input your password: ")
    print(len(user_pass) * '*')
    print("You are welcome to pytBank,  how much would you like to withdraw")
    withdraw_amt = int(input("withdrawal amount: "))

    if (acct_balance >= withdraw_amt):                           
        print("withdrawl amount of ", withdraw_amt, "successful you have ",acct_balance-withdraw_amt, "left")
    else:
        (acct_balance < withdraw_amt)
        print("insufficient fund, go and make money")
else:
    print("invalid card, get a valid one")