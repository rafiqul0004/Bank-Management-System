from Bank import Bank, User, Admin

def main():
    bank = Bank()
    admin = bank.add_admin("Rahat", "r@gmail.com", "CTG")
    print(f"Admin: {admin.name} ID for Admin: {admin.admin_id}")
    user1 = bank.create_user("Oggy", "oggay@gmail.com", "DHA", "Saving")
    print(f"User ID for {user1.name}: {user1.account_number}")
    user2 = bank.create_user("Jack", "jack@gmail.com", "KHU", "Current")
    print(f"User ID for {user2.name}: {user2.account_number}")

    while True:
        print("\nWelcome\n")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")
        choice = int(input("Enter Your Option : "))
        if choice == 1:
            account_number = input("Enter Your Account Number: ")
            user = bank.find_user(account_number)
            if user:
                print(f'\nWelcome User: {user.name} Account Number: {user.account_number}\n')
                while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Take Loan")
                    print("5. Transfer Funds")
                    print("6. Transition History")
                    print("7. Logout")
                    ch = int(input("Enter Your Choice : "))
                    if ch == 1:
                        amount = float(input("Enter The Amount : "))
                        print(user.deposit(amount, bank))
                    elif ch == 2:
                        amount = float(input("Enter The Amount : "))
                        print(user.withdraw(amount, bank))
                    elif ch == 3:
                        print(user.check_balance())
                    elif ch == 4:
                        amount = float(input("Enter The Amount : "))
                        print(user.take_a_loan(amount, bank))
                    elif ch == 5:
                        amount = float(input("Enter The Amount : "))
                        receiver_account_number = input("Enter the recipient's account number: ")
                        print(user.transfer_money(receiver_account_number, amount, bank))
                    elif ch == 6:
                        print(user.transition())
                    elif ch == 7:
                        break
                    else:
                        print("Enter a valid choice")
            else:
                print("User Not Found")
        elif choice == 2:
            admin_id = input("Enter Your admin Id : ")
            admin = bank.find_admin(admin_id)
            if admin:
                print(f'\nWelcome Admin : {admin.name} ID: {admin.admin_id}\n')
                while True:
                    print("1. Delete User Account")
                    print("2. User account List")
                    print("3. Check Total Bank Balance")
                    print("4. Check The Total Loan Amount")
                    print("5. Update Loan Feature")
                    print("6. Logout")
                    ch = int(input("Enter Your Option : "))
                    if ch == 1:
                        user_account_number = input("User account number : ")
                        print(bank.delete_account(user_account_number))
                    elif ch == 2:
                        users = bank.users_list()
                        for user in users:
                            print(f'Username: {user.name} Account_no: {user.account_number} Balance: {user.balance}')
                    elif ch == 3:
                        print(bank.total_bank_balance())
                    elif ch == 4:
                        print(bank.total_loan_amount())
                    elif ch == 5:
                        print(bank.off_loan_feature())
                    elif ch == 6:
                        break
                    else:
                        print("Enter A valid Option")
            else:
                print("No Admin Found")
        elif choice == 3:
            break
        else:
            print("Enter a valid Option")

if __name__ == "__main__":
    main()
