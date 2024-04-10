#Let's learn OOP. Here is an example: Car is a class and color, model, make, engine, etc. are objects within class. Here is another example: Person is a class and name, age, birth date, SSN will be considered at Objects. So, class is a Property or data. 
# Function within the class will be treated as an output based on the input.

class Atm: 
    # There are two things you need to use ATM: Balance and Pincode
    def __init__(self): 
        self.balance = 0
        self.pinCode = ""
        self.menu()
    def menu(self):
        user_input = input("""
              Hello, how are you today? Thank you for choosing Chase ATM. How can I help you? Please select the following items by pressing a number on the keyboard. 
              1. Press 1 to Check Balance.
              2. Press 2 to Withdraw.
              3. Press 3 to Generate a new Pin Code. 
              4. Press 4 to Change Pin Code. 
              5. Press 5 to Add funds.
              """)
        if user_input == "1": 
            #Check balance
            self.checkBalance()
        elif user_input == "2":
            #Withdraw Money 
            self.withdrawnAmount()
        elif user_input == "3":
            #Generate a new Pin Code
            self.createPin()
        elif user_input == "4":
            #Change Pin Code 
            self.changePin()
        elif user_input == "5":
            #add funds 
            self.addAmount()
        else: 
            user_input = "e"
            self.exit()
    
    def createPin(self):
        user_pin = input('Enter your pin: ')
        self.pinCode = user_pin
        
        user_balance = int(input("Enter your balance"))
        self.balance = user_balance
        
        print("Pin created successfully.")
        print(f"Your total balance is {self.balance}")
        
        self.menu()
        
    def changePin(self):
        user_change_pin_old = input("Enter your old pin first to confirm: ")
        if user_change_pin_old == self.pinCode:
            user_change_pin_new = input("Enter your new pin: ")
            self.pinCode == user_change_pin_new
            print(f"Pin has been updated with {user_change_pin_new}")
            self.menu()
        else: 
            print("Your old pin does not exist or match.")
        self.menu()
        
    def checkBalance(self):
        print(f"Your current balance is {self.balance}")
        self.menu()
    
    def withdrawnAmount(self):
        user_pin = input("Enter your pin to withdraw")
        if self.pinCode == user_pin: 
            withdrawn_amount = int(input("How much money would you like to withdrawn?"))
            if withdrawn_amount >= self.balance:
                print("You cannot withdraw due to insufficient funds.")
            else: 
                print(f"Your total balance is {self.balance - withdrawn_amount}")
        else: 
            print("please enter correct pin code to proceed further.")
        self.menu()
    
    def addAmount(self):
        addAmountFunds = int(input("How munch money would you like to deposit?"))
        self.balance = self.balance + addAmountFunds
        print(f"You have now total funds of {self.balance}")
        self.menu()
        
    def exit(self):
        exit()
        
bankAtm = Atm()