from datetime import datetime
from src.data_handler import save_expenses, expenses

categories = ["food", "transportation", "entertainment", "others"]

def add_expense(amount, description, category):
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    if category not in categories:
        print("Invalid category. Please choose from:", categories)
        return
    
    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    expenses.append(expense)
    save_expenses()
