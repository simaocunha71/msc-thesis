def valid_date(date):
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
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
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

print(valid_date('03-11-2000'))  # => True
print(valid_date('15-01-2012'))  # => False
print(valid_date('04-0-2040'))  # => False
print(valid_date('06-04-2020'))  # => True
print(valid_date('06/04/2020'))  # => False