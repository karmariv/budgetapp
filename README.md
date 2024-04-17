Create different expenses categories and add/withdrow amounts to keep control of the balance

![image](https://github.com/karmariv/budgetapp/assets/19791050/21abab63-e8d3-4abb-aeae-67406d0faa81)

Thee function allows to print the balance detail and a graphical  representation of the distribution of expenses

![image](https://github.com/karmariv/budgetapp/assets/19791050/704d786b-dccb-4bd3-bf99-2ad2175c3b40)

The class has the following methods:
- deposit: Accepts and amount and description Description is empty string by  default The object appended to the ledger list
- withdraw: Accepts and amount and description, but amount is passed as negative number. If there are not enough funds nothing should be added to the leger. This method returns TRUE if the withdrawal took place, and FALSE otherwise
- get_balance: Returns the current balance of the budget category
- transfer: Accepts an amount and another budget category as arguments.
- check_funds: Accepts an amount as an argument.It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
- create_spend_chart: reates a graphic represtation showing the % spent on each category.
        
