    import re

    match = re.match(r'(\d{2})-(\d{2})-(\d{4})', date)

    if match is None:
        return False

    month, day, year = map(int, match.groups())

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if month in {4, 6, 9, 11} and day > 30:
        return False
    elif month == 2 and day > 29:
        return False
    elif day > 31:
        return False

    return True


