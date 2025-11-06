import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    FORMAT = "%d-%m-%Y"

    # Initialize the CSV file and reads it, if it exists.
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False) # Export the DataFrame to a CSV file.

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry  = { # Dictionary containing the new entry.
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        } # Opened CSV file in 'append' mode.
        with open(cls.CSV_FILE, mode="a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # Parse dates with the expected format; coerce invalid dates to NaT
        df["Date"] = pd.to_datetime(df["Date"], format=CSV.FORMAT, errors="coerce")
        # Count and optionally inform about invalid date rows
        invalid_dates = df["Date"].isna().sum()

        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        # Filter only valid dated rows first
        valid_df = df.dropna(subset=["Date"]).copy()
        mask = (valid_df["Date"] >= start_date) & (valid_df["Date"] <= end_date)
        filtered_df = valid_df.loc[mask]

        if filtered_df.empty:
            print("No transactions found between the specified dates.")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            if invalid_dates:
                print(f"Note: {invalid_dates} row(s) had invalid dates and were skipped.")
            print(
                filtered_df.to_string(
                    index=False, formatters={"Date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary:")
            print(f"Total Income: £{total_income:.2f}")
            print(f"Total Expense: £{total_expense:.2f}")
            print(f"Net Savings £{(total_income - total_expense):.2f}")

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date (DD-MM-YYYY): or press Enter to use today's date:", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    df.set_index('date', inplace=True)

    income_df = (
        df[df['category'] == 'Income']
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    expense_df = (
        df[df['category'] == 'Expense']
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label='Income', color="g")
    plt.plot(expense_df.index, expense_df["amount"], label='Expense', color="r")
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income & Expenses')
    plt.legend() # Enables the legend
    plt.grid(True) # Enables the grid
    plt.show() # Shows the plot


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = input("Enter the start date (DD-MM-YYYY): ")
            end_date = input("Enter the end date (DD-MM-YYYY): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to plot the transactions? (y/n): ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()