class Category:
    def __init__(self, name):
        self.name = name
        self.balance_amount = 0
        self.deposit_ledger = []
        
    def __str__(self) -> str:
        self.ledger = str(self.name).center(30,"*") + "\n"

        for item in self.deposit_ledger:
           self.ledger = self.ledger + str(item["description"][:23]).ljust(23) + str(item["amount"]).rjust(7) + "\n"

        self.ledger = self.ledger + "Total".ljust(23) + str(round(self.balance_amount,2)).rjust(7)
        
        return self.ledger

    #deposit method        
    def deposit(self, amount, description = ""):
        #update ledger
        self.deposit_ledger.append( {"amount":amount, "description":description})
        
        #update balance amount
        self.balance_amount = self.balance_amount + amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            #update ledger & balance amount
            self.deposit_ledger.append( {"amount":amount*-1, "description":description})
            self.balance_amount = self.balance_amount - amount
            return True
        
        return False

    def get_balance(self):
        return self.balance_amount
    
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        
        return False
    
    def check_funds(self, amount):
        if self.balance_amount - amount < 0:
            return False
        
        return True
            


    
    
    




    #def create_spend_chart(categories):