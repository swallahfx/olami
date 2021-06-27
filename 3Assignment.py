# #palindrome

# print("Welcome, let's check if your word is a palindrome")
# is_entry = input("input any word: ")
# is_entlist = list(is_entry)
# is_entcopy = is_entlist.copy()
# is_entlist.reverse()

# if is_entlist == is_entcopy:
#       print("your entry is a palindrome!")
# else: print("fuck-off!, this isn't a palindrome")




#life left calculator

# print("You are welcome, let's calculate how much life you have left")
# current_age = int(input("How old are you now dear? "))
# life_left = 90 - current_age
# print("you have",life_left, "years")
# print(life_left * 12, "months left") 
# print(life_left * 52, "weeks left")
# print(life_left * 365, "days left")

# print("You are welcome, let's calculate how much life you have left")

def time_left(current_age = int(input("How old are you now dear? "))):
    life_left = 90 - current_age
    print("you have \n",life_left, "years left \n",life_left * 12, "months left \n",life_left * 52, "weeks left \n",life_left * 365, "days left\n\n")

time_left()   

# #ATM collector
def atm():
    import getpass

    
    acct_balance = 10000
    print("YOU ARE WELCOME TO pytBank \n",)
    user_name = input("pls, input Account name: ")
    user_title = input('your title: ')
    card_num= getpass.getpass("pls, input your card number: ")

    if (card_num[0] == "5" and len(card_num) == 16):
        print("you have a Mastercard \n")                              
        user_pass = getpass.getpass("pls, input your password: ")
        print(len(user_pass) * '#')
        transact = input(f"You are welcome to pytBank, {user_title} {user_name} select 1 or 2 \
            \n 1. check balance \
            \n 2. cash withdrawal \n\
            \n choose an option: ")
        if transact == "1":
            print(user_title, user_name, "Your balance is #", acct_balance , "\
            \nTHANK YOU FOR BANKING WITH US")
            atm()
        elif transact == "2":
            withdraw_amt = int(input("pls, input withdrawal amount: #"))
            if acct_balance >= withdraw_amt :                        
                print("withdrawal amount of #", withdraw_amt, "is successful. \n \nyour balance is #",acct_balance - withdraw_amt, "\n\n Thank you for banking with us",user_title , user_name  )
            else:
                (acct_balance < withdraw_amt)
                print("insufficient fund, thank you for banking with us")
                atm()
    elif (card_num[0] == "4") and (len(card_num) == 14):
        print("you have a Visa_card \n")                              
        user_pass = getpass.getpass("pls, input your password: ")
        print(len(user_pass) * '#')
        transact = input(f"You are welcome to pytBank, {user_title} {user_name} select 1 or 2 \
            \n 1. check balance \
            \n 2. cash withdrawal \n\
            \n choose an option: ")
        if transact == "1":
            print(user_title, user_name, "Your balance is #", acct_balance , "\
            \nTHANK YOU FOR BANKING WITH US")
            atm()
        elif transact == "2":
            withdraw_amt = int(input("pls, input withdrawal amount: #"))
            if acct_balance >= withdraw_amt :                        
                print("withdrawal amount of #", withdraw_amt, "is successful. \n \nyour balance is #",acct_balance - withdraw_amt, "\n\n Thank you for banking with us",user_title , user_name  )
            else:
                (acct_balance < withdraw_amt)
                print("insufficient fund, thank you for banking with us")
                atm()
    elif (card_num[0] == "5" and len(card_num) == 19):
        print("you have a Verve_card \n")                              
        user_pass = getpass.getpass("pls, input your password: ")
        print(len(user_pass) * '#')
        transact = input(f"You are welcome to pytBank, {user_title} {user_name} select 1 or 2 \
            \n 1. check balance \
            \n 2. cash withdrawal \n\
            \n choose an option: ")
        if transact == "1":
            print(user_title, user_name, "Your balance is #", acct_balance , "\
            \nTHANK YOU FOR BANKING WITH US")
            atm()
        elif transact == "2":
            withdraw_amt = int(input("pls, input withdrawal amount: #"))
            if acct_balance >= withdraw_amt :                        
                print("withdrawal amount of #", withdraw_amt, "is successful. \n \nyour balance is #",acct_balance - withdraw_amt, "\n\n Thank you for banking with us",user_title , user_name  )
            else:
                (acct_balance < withdraw_amt)
                print("insufficient fund, thank you for banking with us")
                atm()
    else:
        print("invalid card, get a valid one \n \n")
        atm()
    #card_num= input("pls, input valid card number: ")


atm()



# print("You are welcome to pytBank,  how much would you like to withdraw")
# withdraw_amt = int(input("withdrawal amount: ")

# if (acct_balance >= withdraw_amt):                           
#     print("withdrawl amount of ", withdraw_amt, "successful you have "acct_balance-withdraw_amt, "left")
# else:
#     (acct_balance < withdraw_amt)
#     print("insufficient fund, go and make money")


# while (card_num[0] != 5 and len(card_num) != 16) or (card_num[0] != 4 and len(card_num) != 16) or (card_num[0] != 5 and len(card_num) != 19):
#     card_num= input("pls, Enter a valid card number: ")
#     break
# user_pass = getpass.getpass("pls, input your password: ")
# print(len(user_pass) * '*')
# 

# # password = getpass.getpass()
# # print(password)

# password = getpass.getpass('Enter password: ')


# print(password)
# 

# message = "whats ur fucking name"
# choice = ""
# while choice != "exit":
#     choice = input(message)
#     print("choclate")


