    try:
        month, day, year = map(int, date.replace('-', '/').split('/'))
    except ValueError:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if month in {4, 6, 9, 11} and day > 30:
        return False

    if month == 2:
        if year % 4 == 0 and day > 29:
            return False
        elif day > 28:
            return False

    return True


