import pandas as pd
from src.data_handler import expenses

def summarize_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    df = pd.DataFrame(expenses)
    monthly_summary = df.groupby(df['date'].str[:7])['amount'].sum()
    category_summary = df.groupby('category')['amount'].sum()
    print("\nMonthly Summary:\n", monthly_summary)
    print("\nCategory Summary:\n", category_summary)
