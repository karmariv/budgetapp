# TODO
# Add chart method

class Category:
    def __init__(self, name):
        self.name = name
        self.balance_amount = 0
        self.total_withdraw = 0
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
            self.total_withdraw = self.total_withdraw + amount
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
        
    def get_total_withdraw(self):
        return self.total_withdraw
        
        return True
            

def create_spend_chart(categories):
    total_withdraw = 0
    scale_min = 0
    scale_max = 100
    scale_step = 10
    symbol = 'o'
    values = {}
    chart = ''

    for el in categories:
        total_withdraw = total_withdraw + el.get_total_withdraw()

    for el2 in categories:
        size = round((el2.get_total_withdraw() / total_withdraw * 100/scale_step),0)
        values[el2.name] = size

        
    step = scale_min
    xaxis_size = 0
    xaxis = ""
    category_name_max_size = 0
    while step <= scale_max:
        dummy =  (str(scale_max - step) + '|').rjust(4)

        for k,v in values.items():
            if (scale_max - step) / scale_step  <= v:
                dummy = dummy + symbol.center(3)
                xaxis_size = xaxis_size + 3

            if len(k) > category_name_max_size:
                category_name_max_size = len(k)
                    
        step = step + scale_step

        chart = chart + dummy + '\n'

    chart = chart + xaxis.center(4) +  xaxis.rjust(len(values)*3, '-') + '\n'

    j = 0
    
    while j < category_name_max_size:
        axis_labels = ''.center(4)
       
        for k,v in values.items():
       
            if j < len(k):
                axis_labels = axis_labels + k[j].center(3) 
            else:
                axis_labels = axis_labels + "".center(3)
       
        chart = chart + axis_labels + '\n'    

        j = j + 1    

    return chart

