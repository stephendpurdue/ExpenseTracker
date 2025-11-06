import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]

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
        } # Opened CSV file in append mode.
        with open(cls.CSV_FILE, mode="a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")


CSV.initialize_csv()
CSV.add_entry("06-22-2025", 125.65, "Income", "Salary")