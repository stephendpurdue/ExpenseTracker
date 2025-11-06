from datetime import datetime

date_format = "%D-%M-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

# Gets date from user.
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try: # Takes the date string, using this format, and converts it to a datetime object.
        valid_date = datetime.strptime(date_str, date_format)
    except ValueError:
        print("Invalid date format. Please use the following format: DD-MM-YYYY.")
        return get_date(prompt, allow_default)

    # This function is recursive, meaning it runs until a valid date is entered.

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.") # Checks if the amount is greater than zero.
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category: ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()


def get_description():
    return input("Enter a description: (Optional) ")
