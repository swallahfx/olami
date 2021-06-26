


ask_num = input("pick 2 digit numbers between 10 and 99: ")

if  len(ask_num) > 2:
        new_entry1 = input("sorry, input digit with 2 values: ")
        ask_num = new_entry1
        

elif    len(ask_num) < 2:
        new_entry1 = input("sorry, input 2 digit nos: ")
                
                
elif    ask_num.isalpha():
        new_entry1 = input("sorry, input num not alphabet: ")
                
                
elif    int(ask_num) > 10 and int(ask_num) <100:
        first_num = int(str(ask_num)[0])
        second_num = int(str(ask_num)[1])
        final = first_num + second_num
        if (final >= 0  and final <= 9):
                print(final," is correct. you win!")
                
        else:
                print("two digits but you lose!")
                new_entry1 = ask_num
                new_entry1 = input("sorry, input number again ")       
                
else:
        while(False):
                new_entry1 = input("sorry, keep trying")
                new_entry1 = ask_num
        # else:
        #     while ask_num is not True: 
                

# elif    ask_num == list(ask_num):
#         sum_ofnumber =0
#         for i in ask_num:
#             sum_ofnumber +=i
#             print(sum_ofnumber)
#             if  (sum_ofnumber >= 0  and sum_ofnumber <= 9):
#                 print(sum_ofnumber," is correct. you win!")
#             else:print("two digits but you lose!")


