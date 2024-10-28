def valid_date(date):
    # Check if date is not empty
    if not date:
        return False

    # Check if date is in the correct format
    if not '-' in date:
        return False

    # Split the date into month, day, and year
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Convert month, day, and year to integers
    try:
        month, day, year = int(month), int(day), int(year)
    except ValueError:
        return False

    # Check if month is valid
    if month < 1 or month > 12:
        return False

    # Check if day is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    else:
        return False

    # Return True if all checks pass
    return True

print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False