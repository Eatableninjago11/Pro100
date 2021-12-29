pin = 100
balance = 100
askPin = int(input("Enter The Pin: "))

if askPin==pin:
    print(balance)
    number = int(input("Press 1 to withdraw, press 2 to deposit: "))
    if number ==1:
        withdraw = int(input("Amount To Withdraw: "))
        if withdraw>balance:
            print("Insufficent Funds")
        else:
            print("Withdraw Complete")
            print(balance-withdraw)
    else:
        deposit = int(input("Enter Amount to Deposit: "))
        print("Deposit Complete")
        print(balance + deposit)
        
else:
    print("The pin doesn't Match")