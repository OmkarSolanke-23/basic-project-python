
balance = 5000

while True :

    print("\n --- ATM ---")
    print("1. check balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. Exit")

    choice = input("Please Enter The choice : ")

    try :

        if choice =="1":
            print("Balance : " , balance)

        elif choice == "2":
            amount = float(input("Enter amount: "))

            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            balance += amount
            print("Deposit successful")

        elif choice == "3":
            amount = float(input("Enter amount: "))

            if amount > balance:
                raise Exception("Insufficient balance")

            balance -= amount
            print("Withdrawal successful")

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please try again.")
    except ValueError as e:
        print("Error:", e)
    except Exception as e: 
        print("Error:", e)