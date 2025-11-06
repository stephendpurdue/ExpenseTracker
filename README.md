# ExpenseTracker

A simple command-line tool to track your personal income and expenses in a CSV file and optionally visualize them. The app lets you:

- Add transactions (date, amount, category, description)
- View a filtered list of transactions for a date range
- See totals (income, expense, and net savings)
- Optionally plot income vs expense over time


## Requirements
- Python 3.13+ (recommended)
- pip

Python packages:
- pandas
- matplotlib


## Installation
It’s recommended to use a virtual environment.

1) Clone or download this repository.
2) Open a terminal in the project folder: `C:\Users\steph\PycharmProjects\ExpenseTracker`.
3) Create and activate a virtual environment (Windows PowerShell):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4) Install dependencies:
```
pip install pandas matplotlib
```


## Usage
Run the application:
```
python main.py
```

You will see a menu with options:

1. Add a new transaction
   - You’ll be prompted for:
     - Date in DD-MM-YYYY format (press Enter to use today’s date when prompted)
     - Amount (positive number)
     - Category (Income or Expense)
     - Description (free text)

2. View transactions
   - Enter a start and end date in DD-MM-YYYY format.
   - The app prints all transactions within that range, along with a summary of total income, total expense, and net savings.
   - You may be prompted to plot the transactions (requires matplotlib). If chosen, a line plot of daily income vs expense is displayed.

3. Exit


## Data Storage
Transactions are stored in a CSV file named `finance_data.csv` in the project root. The columns are:

- Date (DD-MM-YYYY)
- Amount (numeric)
- Category (Income or Expense)
- Description (text)

Example row:
```
Date,Amount,Category,Description
06-11-2025,1200.00,Income,Salary
06-11-2025,45.50,Expense,Groceries
```


## Notes and Tips
- Date format matters: use DD-MM-YYYY (e.g., 06-11-2025). Rows with invalid dates will be skipped when viewing a range.
- If you get an error when plotting, ensure `matplotlib` is installed (`pip install matplotlib`) and a display is available.
- If you manually edit the CSV, keep the header row and column names unchanged.
- Currency symbol in summaries is "£" by default in print output.


## Troubleshooting
- Module not found (pandas/matplotlib): Ensure your virtual environment is activated and dependencies installed.
- Unicode or encoding issues when opening the CSV: Save the file in UTF-8 without BOM if edited externally.
- Nothing displays for a date range: Verify the dates are entered as DD-MM-YYYY and that data exists in that range.


## Project Structure
```
ExpenseTracker/
├─ main.py            # App entry point and CLI
├─ data_entry.py      # Input helpers (date, amount, category, description)
├─ finance_data.csv   # Data file (created automatically if missing)
└─ README.md          # This file
```


## Contributing
Issues and pull requests are welcome. Please keep changes focused and include clear descriptions.