balance = 0.0

while True:
    print("\nATM Menu: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Welcome to ABC Bank, Choose an action: ")

    try:
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"${amount} Deposited!")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"${amount} withdrawn!")
        elif choice == "3":
            print(f"Your Balance is ${balance}")
        elif choice == "4":
            print("Have a great day ahead!")
            break
        else:
            print("Invalid choice! Choose a valid option: ")
    except ValueError:
        print("Please enter a valid number! ")
