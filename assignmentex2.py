acct_balance = 10000
withdraw_amt = 0
if (acct_balance >= withdraw_amt):                           
    print("withdrawl amount of ", withdraw_amt, "successful you have "acct_balance - withdraw_amt, "left")
elif (acct_balance < withdraw_amt):
    print("insufficient fund, go and make money")

