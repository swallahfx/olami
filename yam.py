
# number = input("enter number")
# while (number.isalpha() or len(number) >2 or len(number) < 2 or "." in number() or number[0] == "-"):
#         if number.isalpha():
#                 number = input("number is alpha")
#         elif "." in number:
#                 number = input("number is a float")
#         elif len(number) >2 or len(number)<2:
#                 number = input("number is > or < than 2 digit")
#         elif number[0] == "-":
#                 number = input("number is negative")
# prev_number = number
# sum_of_numbers = int(number[0]) + int(number[1])
# while sum_of_numbers > 9:
#         number = input("number is greater than 9")
#         sum_of_numbers = int(number[0]) + int(number[1])
# print(sum_of_numbers)


num = input('''
input num''')
while len(num) != 5 and num[:3] != '234':
        num = input('''
input num''')
print('correct')




        # if (prev_number != number):
        #         print(sum_of_numbers, "you win")
        # else:
        #         number = input("enter number")
# num = input('''
# input num ''')
# while num[:3] != 234 and len(num) != 13:
#        num = input('''
#        input num ''') 
       
# print('valid num')
        