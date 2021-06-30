bank_balance = 10000
transfer_amount = 0
welcome = input(''' 
    Welcome to USSD Banking, Please note a N6.98
    network charge will be applied to your account
    for banking service on this channel
    1. Accept
    2. Cancel  ''')
def self_service():
    global bank_balance
    # bank_balance = 10000
    global transfer_amount

    if welcome == '1':
        service1 = input(''' 
        1. Airtime-self
        2. Airtime-others
        3. Check balance '''   )
        if service1 == '1':

            
            amount = int(input('''
            pls enter amount '''))
            f_bal = bank_balance - amount
            print(f'''
            Your airtime transfer of {amount} is successful.
            you have {f_bal} left in your account 
            go cashless with 737 USSD! Dial *737*1# to send
            money to GTB accounts and  *737*2# to other bank accounts
            ''')
            f_bal = bank_balance - amount
            bank_balance = f_bal
            re_run = input('''
            Would you like to perform another transaction
            if yes enter 1 or enter 0 to cancel 
            ''')
            if re_run == '1':
                self_service()
            if re_run == '0':
                exit()
        elif service1 == '2':
            third_party_num = input('''
            Please enter Third party mobile number ''')
            while third_party_num[0:3] is not '+234' and len(third_party_num) != 14:
                third_party_num = input('''
            Invalid Third party mobile number,
            Please enter correct mobile number ''')
            third_party_num = third_party_num
            transfer_amount = int(input('''
            Pls enter amount: N '''))
            if transfer_amount <= bank_balance:
                pin_code = input(f'''
            Enter your 737 PIN or Token code to top up {third_party_num}.
            with N {transfer_amount} or enter 0 to cancel ''')

                while pin_code != '1234':
                    pin_code = input(f'''
            Enter valid 737 PIN or Token code to top up {third_party_num}.
            with N {transfer_amount} or enter 0 to cancel ''')
                final_transfer = bank_balance - transfer_amount
                bank_balance= final_transfer
                return_val = input(f'''
                    Transfer amount of N {transfer_amount} was successful.
                    Would you like to perform another transaction if yes 
                    enter 1 or enter 0 to cancel ''')
                bank_balance= final_transfer
                if return_val == '1':
                    self_service()
                exit()

                if pin_code == '0':
                    exit()
            else:
                print("insufficient fund")
                self_service()



        
        elif service1 == '3':
            final_transfer = bank_balance - transfer_amount
            bank_balance = final_transfer
            pin_code = input('''
            Enter your 7377 PIN or Token code to check your balance.
            please note a N10 network charge will deducted from
            your account for this service ''' )
            while len(pin_code)!= 4:
                third_party_num = input('''
            Invalid PIN,
            Please enter correct 7377 PIN ''')
            balance = input(f''' 
            Your Account balance is {final_transfer}
            Would you like to perform another transaction
            if yes enter 1 or enter 0 to cancel ''')
            if balance == '1':
                self_service()
            if balance == '2':
                exit()

    elif welcome == '2':
        exit()
self_service()











    # third_party_num = input('''
    #     Please enter third party mobile number: ''')
    # while third_party_num != '08104048682': 
    #     third_party_num = input('''Please enter a valid third party mobile number: ''')
    #     third_party_num = third_party_num
    # print("valid Mtn Number: ")


        