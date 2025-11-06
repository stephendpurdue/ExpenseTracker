from datetime import datetime

date_format = "%D-%M-%Y"

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
    pass


def get_category():
    pass


def get_description():
    pass
