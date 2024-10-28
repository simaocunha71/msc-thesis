    month, day, year = [int(s) for s in date.split('-')]
    if len(date) != 10 or month < 1 or month > 12 or day < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False
    elif month == 2:
        if day > 28: # or day > 29 in leap year
            return False
    elif day > 29: # for month 0 and month > 12
        return False

    if year < 0:
        return False

    return True


