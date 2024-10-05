
def valid_date(date):
    # Splitting the date string
    date_string = date.split('-')

    # Checking if the date string is not empty
    if len(date_string) != 3:
        return False

    # Converting the month, day and year to integers
    month = int(date_string[0])
    day = int(date_string[1])
    year = int(date_string[2])

    # Checking if the months are between 1 and 12
    if month < 1 or month > 12:
        return False

    # Checking if the days are valid for each month
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if day < 1 or day > 31:
            return False
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        if day < 1 or day > 30:
            return False
    elif (month == 2):
        if day < 1 or day > 28:
            return False

    # Checking if the year is a four-digit number
    if len(str(year)) != 4:
        return False

    # If all the above conditions are satisfied then the date is valid
    return True


# Testing the function
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False

























































