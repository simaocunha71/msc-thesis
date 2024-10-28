    import re

    if not date:
        return False

    pattern = re.compile('^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$')

    if not pattern.match(date):
        return False

    month, day, year = map(int, date.split('-'))

    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2:
        if day > 29:
            return False
    elif day > 31:
        return False

    return True


