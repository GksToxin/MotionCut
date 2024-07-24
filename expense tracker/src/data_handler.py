import json

expenses = []

def save_expenses():
    with open('data/expenses.json', 'w') as file:
        json.dump(expenses, file)

def load_expenses():
    global expenses
    try:
        with open('data/expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
