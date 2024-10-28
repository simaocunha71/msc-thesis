
def valid_date(date):
    if not date:
        return False
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    month, day, year = date_parts
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month in [2]:
        if day < 1 or day > 29:
            return False
    elif day < 1 or day > 31:
        return False
    return True
