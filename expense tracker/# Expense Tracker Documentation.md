# Expense Tracker Documentation

## Overview
The Expense Tracker is a Python application that allows users to input, store, and analyze their daily expenses. It categorizes expenses and provides summaries of spending patterns.

## Features
- Add daily expenses with descriptions and categories.
- Store and retrieve expense data.
- Categorize expenses into predefined categories.
- View monthly and category-wise summaries of expenses.
- User-friendly command-line interface.
- Error handling for invalid inputs.

## How to Use
1. Run the `main.py` file.
2. Follow the on-screen prompts to add expenses or view summaries.
3. The expense data is stored in `data/expenses.json`.

## Code Structure
- `main.py`: Main entry point of the application.
- `src/`: Contains the source code for the application.
- `data/`: Contains the data files for storing expenses.

## Key Functions
- `add_expense(amount, description, category)`: Adds an expense to the tracker.
- `save_expenses()`: Saves the expense data to a file.
- `load_expenses()`: Loads the expense data from a file.
- `summarize_expenses()`: Provides summaries of expenses.

## Conclusion
This project enhances understanding of Python programming concepts and practical application development, focusing on data management, user interaction, and data analysis.
