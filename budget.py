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
        """
        Accepts and amount and description
        Description is empty string by  default
        The object appended to the ledger list

        Arguments:
        amount 
        description 
        """
        #update ledger
        self.deposit_ledger.append( {"amount":amount, "description":description})
        
        #update balance amount
        self.balance_amount = self.balance_amount + amount

    def withdraw(self, amount, description = ""):
        """
        Accepts and amount and description, but amount is passed as negative number. If there are not enough funds nothing should be added to the leger
        This method returns TRUE if the withdrawal took place, and FALSE otherwise

        Arguments:
        amount 
        description 

        Return Boolean
        """

        if self.check_funds(amount) == True:
            #update ledger & balance amount
            self.deposit_ledger.append( {"amount":amount*-1, "description":description})
            self.balance_amount = self.balance_amount - amount
            self.total_withdraw = self.total_withdraw + amount
            return True
        
        return False

    def get_balance(self):
        """
        Returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        """
        return self.balance_amount
    
    def transfer(self, amount, category):
        """
        Accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount 
        and the description "Transfer to [Destination Budget Category]". The method adds a deposit to the other budget 
        category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, 
        nothing is added to either ledgers. 

        This method returns True if the transfer took place, and False otherwise.
        
        Arguments:
        amount 
        category 
        
        Return Boolean
        
        """
        
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        
        return False
    
    def check_funds(self, amount):
        """
        Accepts an amount as an argument.
        It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        """

        if self.balance_amount - amount < 0:
            return False
        
        return True
        
    def get_total_withdraw(self):
        return self.total_withdraw
        
        return True
            

def create_spend_chart(categories):
    """
    Creates a graphic represtation showing the % spent on each category.

    categories

    Return as string simulating a graphical represention
    """
    
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

