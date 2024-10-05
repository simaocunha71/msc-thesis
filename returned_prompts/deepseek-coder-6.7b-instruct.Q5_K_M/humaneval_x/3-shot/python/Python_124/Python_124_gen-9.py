    if not date:
        return False

    parts = re.split('-', date)
    if len(parts) != 3:
        return False

    month, day, year = parts

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month, day, year = int(month), int(day), int(year)

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
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                return True
            else:
               