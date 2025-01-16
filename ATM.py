class ATM:
    def __init__(self):
        self.balance = 5000 # Balance = 5000
        self.pin = '1234' # Default PIN = 1234
        self.transaction_history = []  # Empty list to store transaction history
    
    def display_options(self):
        # Displays the menu options to the user
        print("\nATM")
        print("1. Check Balance") # Check the current balance
        print("2. Withdraw Cash") # Withdraw cash
        print("3. Deposit Cash") # Deposit cash
        print("4. Change PIN") # Change the PIN
        print("5. Transaction History") # View the transaction history
        print("6. Exit") # Exit the ATM

# Check and display the balance of the user
    def check_balance(self):
        print(f"Your current balance is Rs. {self.balance}")

# Allows the user to withdraw cash
    def withdraw_cash(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew Rs. {amount}")
            print(f"Withdrew Rs. {amount}. Remaining balance is Rs. {self.balance}")
        else:
            print("Insufficient balance")

# Allows the user to deposit cash
    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited Rs. {amount}")
            print(f"Deposited Rs. {amount}. New Balance is Rs. {self.balance}")
        else:
            print("Invalid amount")
# Allows the user to change the PIN
    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("Incorrect Pin")
            return
        
        if len(str(new_pin)) != 4:
            print("New PIN must be 4 digits, Please try again")
            return
        
        self.pin = new_pin
        print("PIN successfully changed")

# Allows the user to view transaction history
    def view_transaction_history(self):  # Renamed method to avoid conflict
        if not self.transaction_history:
            print("No transactions yet.")
            return
        
        print("Transaction history: ")
        for transaction in self.transaction_history:
            print(transaction)

# Main function to simulate the ATM
def atm_simulation():
    atm = ATM()
    print("Welcome to the ATM")
    while True:
        # Display the menu with options
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

         # If the user chooses option 1, check the balance
        if choice == '1':
            atm.check_balance()

        # If the user chooses option 2, deposit cash
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: Rs. "))
                atm.deposit_cash(amount)  
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # If the user chooses option 3, withdraw cash
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: Rs. "))
                atm.withdraw_cash(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # If the user chooses option 4, change the PIN
        elif choice == '4':
            try:
                old_pin = input("Enter your current PIN: ")
                new_pin = input("Enter your new 4-digit PIN: ")
                atm.change_pin(old_pin, new_pin)
            except ValueError:
                print("Invalid Input. Please enter a valid number.")

        # If the user chooses option 5, view transaction history
        elif choice == '5':
            atm.view_transaction_history()
        
        # If the user chooses option 6, exit the program
        elif choice == '6':
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid option. Please try again")

# Main block to run the ATM simulation
if __name__ == "__main__":
    atm_simulation()