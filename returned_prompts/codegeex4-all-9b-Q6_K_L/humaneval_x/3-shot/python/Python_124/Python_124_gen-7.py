    import re

    pattern = r'^([1-9]|0[1-9]|1[0-2])-([1-9]|0[1-9]|[12][0-9]|3[01])-[0-9]{4}$'
    if re.match(pattern, date):
        month, day, year = map(int, date.split('-'))
        if month == 2:
            if day > 29:
                return False
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
        elif day > 31:
            return False
        return True
    return False

