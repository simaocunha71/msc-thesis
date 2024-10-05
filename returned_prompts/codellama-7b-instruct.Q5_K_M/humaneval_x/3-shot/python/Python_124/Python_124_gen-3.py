    if not date:
        return False

    if len(date.split('-')) != 3:
        return False

    day, month, year = date.split('-')

    if int(month) < 1 or int(month) > 12:
        return False

    if int(day) < 1 or int(day) > 31:
        return False

    if int(year) < 0 or int(year) > 9999:
        return False

    if int(month) in [4, 6, 9, 11] and int(day) < 1 or int(day) > 30:
        return False

    if int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) < 1 or int(day) > 31:
        return False

    if int(month) == 2 and int(day) < 1 or int(day) > 29:
        return False

    return True


