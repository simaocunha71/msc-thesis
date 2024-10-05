def valid_date(date):
    if not date:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    month, day, year = map(int, parts)
    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if year % 4 == 0 and day > 29:
            return False
        elif year % 4 != 0 and day > 28:
            return False

    return True

print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False