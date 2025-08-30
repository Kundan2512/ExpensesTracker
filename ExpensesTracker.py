import ExpensesService as expensesUtil


if __name__=="__main__":
    MENU = """
    Personal Expense Tracker
    ------------------------
    1) Add expense
    2) View expenses
    3) Track budget
    4) Save expenses
    5) Exit
    """
    expensesUtilObject = expensesUtil.Expenses()
    while True:
       try:
           print(MENU)
           choice = int(input("Enter your choice(1 to 5): "))
           if choice == 1:
               expensesUtilObject.addExpense()
           elif choice == 2:
               expensesUtilObject.getExpenses()
           elif choice == 3:
               expensesUtilObject.trackBudget()
           elif choice == 4:
               expensesUtilObject.saveExpenses()
           elif choice == 5:
               expensesUtilObject.saveExpenses()
               break
           else:
               print("Invalid choice")
       except Exception:
           print("Invalid input")
           print(MENU)
           continue

