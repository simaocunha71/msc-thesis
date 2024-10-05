
def valid_date(date):
    if date == "":
        return False
    if date.count("-") != 2:
        return False
    month, day, year = date.split("-")
    try:
        month, day, year = int(month), int(day), int(year)
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        elif day == 29:
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                return False
    return True


print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
print(valid_date('02-30-2000'))  # False
print(valid_date('02-29-2000'))  # True
print(valid_date('02-29-1900'))  # False
print(valid_date('02-29-2004'))  # True


Note: This function assumes that the date is in the Gregorian calendar system. The function does not check for dates that do not exist in the Gregorian calendar system, such as February 30 or February 31.


The function valid_date(date) takes a string date as input. If the date string is empty, the function returns False. If the date string does not contain exactly two "-" characters, the function also returns False.


The function then splits the date string into