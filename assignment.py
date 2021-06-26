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

# def time_left(current_age = int(input("How old are you now dear? "))):
#     life_left = 90 - current_age
#     print("you have",life_left, "years")
#     print(life_left * 12, "months left") 
#     print(life_left * 52, "weeks left")
#     print(life_left * 365, "days left")

# time_left()   

# #ATM collector


# import random

# nump = random.randint(1000, 9999)
# print(nump)
# n = int(input("Enter four digit: "))

# while n != 10:
#     num = nump
#     cor = 0
#     while num % 10:
#         numc = num % 10
#         nc = n % 10
#         num = num//10
#         n = n//10
#         if numc == nc:
#             cor +=1
#     if cor == 4:
#         print("congrats you get it")
#         break
#     else:
#         print("error, try again")
#         n = int(input("Enter four digit: "))
# else:
#     print("Quit the game")


# x = [1,2,3,4,"mehn"]
# length = 0
# i = 0
# try:
#     while x[i] > 0:
#         length += 1
#         i + 1
#     print(length)
# except IndexError:
#     print(length)


## atm
import getpass

acct_balance = 10000
print("You are welcome to pytBank ")
user_name = input("pls, input your user name: ")
card_num= input("pls, input your card number: ")
if (card_num[0] == 5 and len(card_num) == 16):                              
    user_pass = getpass.getpass("pls, input your password: ")
    print(len(user_pass) * '*')
elif (card_num[0] != 4 and len(card_num) != 16):
    user_pass = getpass.getpass("pls, input your password: ")
    print(len(user_pass) * '*')
elif (card_num[0] != 5 and len(card_num) != 19):
    user_pass = getpass.getpass("pls, input your password: ")
    print(len(user_pass) * '*')
else:
    print("invalid card")
print("You are welcome to pytBank,  how much would you like to withdraw")
withdraw_amt = int(input("withdrawal amount: ")

if (acct_balance >= withdraw_amt):                           
    print("withdrawl amount of ", withdraw_amt, "successful you have "acct_balance-withdraw_amt, "left")
elif (acct_balance < withdraw_amt):
    print("insufficient fund, go and make money")

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
