from src.expense_tracker import add_expense
from src.analysis import summarize_expenses

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summaries")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            category = input("Enter category: ")
            add_expense(amount, description, category)
        elif choice == '2':
            summarize_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
