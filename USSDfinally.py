# bank_balance = 10000
# transfer_amount = 0
welcome = input(''' 
    Welcome to USSD Banking, Please note a N6.98
    network charge will be applied to your account
    for banking service on this channel
    1. Accept
    2. Cancel  ''')
def self_service():
    bank_balance = 10000
    transfer_amount = 0
    if welcome == '1':
        service1 = input(''' 
        1. Airtime-self
        2. Airtime-others
        3. Check balance '''   )
        if service1 == '1':
            amount = input('''
            pls enter amount ''')
            print(f'''
            Your airtime transfer of {amount} is successful . 
            go cashless with 737 USSD! Dial *737*1# to send
            money to GTB accounts and  *737*2# to other bank accounts
            ''')
            re_run = input('''
            Would you like to perform another transaction
            if yes enter 1 or enter 0 to cancel ''')
            if re_run == '1':
                self_service()
            if re_run == '0':
                exit()
        elif service1 == '2':
            third_party_num = input('''
            Please enter Third party mobile number ''')
            while third_party_num[0] != '0' and len(third_party_num) != 11:
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

                if len(pin_code) == 4:
                    final_transfer = bank_balance - transfer_amount
                    final_transfer = bank_balance
                    return_val = input(f'''
                    Transfer amount of N {transfer_amount} was successful.
                    Would you like to perform another transaction if yes 
                    enter 1 or enter 0 to cancel ''')
                    if return_val == '1':
                        self_service()
                    exit()

                if pin_code == '0':
                    exit()




        
        elif service1 == '3':
            final_transfer = bank_balance - transfer_amount
            final_transfer = bank_balance
            pin_code = input('''
            Enter your 7377 PIN or Token code to check your balance.
            please note a N10 network charge will deducted from
            your account for this service ''' )
            while len(pin_code) != 4:
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


        