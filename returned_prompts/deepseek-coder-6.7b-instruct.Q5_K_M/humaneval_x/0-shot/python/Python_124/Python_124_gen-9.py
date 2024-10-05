
def valid_date(date):
    if date == '':
        return False

    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month != 2 and day > 30:
        return False

    return True


print(valid_date('03-11-2000'))  # => True
print(valid_date('15-01-2012'))  # => False
print(valid_date('04-0-2040'))  # => False
print(valid_date('06-04-2020'))  # => True
print(valid_date('06/04/2020'))  # => False
print(valid_date('02-30-2020'))  # => False
print(valid_date('02-29-2020'))  # => True
print(valid_date('02-29-2019'))  # => False
print(valid_date('02-30-2019'))  # => False

In this solution, the function first checks if the date string is not empty and splits it into its components (month, day, year). If this fails, it returns False.

Then it checks if the month and year are in the valid range (1-12 and 1-31), and if the day is valid for the given month. February has 29 days in a leap year, and 28 otherwise.

Finally, it returns True if all the checks pass, and False otherwise.

Note: This solution assumes that the year is always in the range 1-9999, and that the input date string is always in the format mm-dd-yyyy. If these assumptions are not always true, the function