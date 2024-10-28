    date = date.split("-")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2 and day > 29:
        return False

    if month == 2 and day == 29 and year % 4 == 0:
        return True

    if month == 2 and day == 29 and year % 4 != 0:
        return False

    return True


