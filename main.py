def desposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must greater than 0.")
        else:
            print("Please enter a number.")
    return amount

desposit()