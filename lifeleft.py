#life left calculator

print("WELCOME TO OUR TIME-LEFT CALCULATOR")
def time_left():
     current_age = input("How old are you now dear? ")
     try:
        if int(current_age) <= 90:
            life_left = 90 - int(current_age)
            print("you have:\n",life_left, "year left")
            print(life_left * 12, "months left") 
            print(life_left * 52, "weeks left")
            print(life_left * 365, "days left")
        elif int(current_age) > 90:
            print("you input a wrong age dear, try again")
            time_left()    
        elif current_age.isalpha:
            print('invalid input, try again')
            time_left()
     except ValueError:
         print("you input a wrong age dear, try again")
         time_left()    

time_left()  









# def time_left(current_age = int(input("How old are you now dear? "))):
#     life_left = 90 - current_age
#     print("you have \n",life_left, "years left \n",life_left * 12, "months left \n",life_left * 52, "weeks left \n",life_left * 365, "days left\n\n")

# time_left()  