# welcome = input(''' 
# Welcome to USSD Banking, Please note a N6.98
# network charge will be applied to your account
# for banking service on this channel
# 1. Accept
# 2. Cancel  ''')
# bank_balance = 10000
# if welcome == '1':
#     service1 = input(''' 
#     1. Airtime-self
#     2. Airtime-others
#     3. Check balance '''   )
#     if service1 == '1':
#         amount = int(input('''
#         pls enter amount '''))
#         print('''
#         Your request is processing. go cashless with
#         737 USSD! Dial *737*1# to send money to GTB accounts
#         and  *737*2# to other bank accounts''')
#     elif service1 == '2':
#         third_party_num = input('''
#         Please enter Third party mobile number''')
#         while third_party_num[0] != '0' and len(third_party_num) != 11:
#            third_party_num = input('''
#         Invalid Third party mobile number,
#         Please enter correct mobile number ''')
#            third_party_num = third_party_num
#         transfer_amount = int(input('''
#         Pls enter amount: '''))
#         if transfer_amount <= bank_balance:
#             pin_code = input(f'''
#         Enter your 737 PIN or Token code to top up {third_party_num}.
#         with N {transfer_amount} or enter 0 to cancel''')

#             if len(pin_code) == 4:
#                 final_transfer = bank_balance - transfer_amount
#                 return_val = input(f'''
#                 Transfer amount of N {final_transfer} was successful.
#                 Would you like to perform another transaction if yes 
#                 enter 1 or enter 0 to cancel ''')
#                 while return_val == '1':
#                     service = input(''' 
#                 1. Airtime-self
#                 2. Airtime-others
#                 3. Check balance '''   )
#                     service = service1
#                 exit()

#             if pin_code == '0':
#                 exit()





#     elif service1 == '3':
#         pin_code = input('''
#         Enter your 7377 PIN or Token code to check your balance.
#         please note a N10 network charge will be
#         applied to your account for this service''' )
# elif welcome == '2':
#     exit()












# # third_party_num = input('''
# #     Please enter third party mobile number: ''')
# # while third_party_num != '08104048682': 
# #     third_party_num = input('''Please enter a valid third party mobile number: ''')
# #     third_party_num = third_party_num
# # print("valid Mtn Number: ")


#mtn number check
num = (input("input ur num lets check"))
fnum = list(num)
while (fnum[0]) != '0' :
    num = (input("input ur num lets check"))
print('its mtn')

#int(fnum[0]) != 0 and int(fnum[1]) != range(7,10) and int(fnum[2]) != range(0,2) and int(fnum[3]) != range(3,5) and int(fnum[3]) !=6: 