

ask_num = input("pick 2 digit numbers between 10 and 99: ")

if      len(ask_num) > 2:
        new_entry2 = input("error, input digit with 2 values: ")


elif    len(ask_num) < 2:
        new_entry2 = input("error, input 2 digit nos: ")


elif    int(ask_num) > 10 and int(ask_num) <100:
        first_num = int(str(ask_num)[0])
        second_num = int(str(ask_num)[1])
        final = first_num + second_num
        if  (final >= 0  and final <= 9):
            print(final," is correct. you win!")

        else:print("two digits but you lose!")

elif    ask_num.isalpha:
        new_entry1 = input("error, input num not alpha: ")

else:
        while ask_num is not True: 
            new_entry1 = input("error, keep trying")
