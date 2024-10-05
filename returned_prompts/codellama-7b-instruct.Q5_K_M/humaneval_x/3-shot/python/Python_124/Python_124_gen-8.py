    month, day, year = date.split('-')

    if int(day) > 31 or int(day) < 1:
        return False

    if int(month) == 2:
        if int(day) > 29 or int(day) < 1:
            return False
    elif int(month) in [4,6,9,11] and int(day) > 30 or int(day) < 1:
        return False
    elif int(month) in [1,3,5,7,8,10,12] and int(day) > 31 or int(day) < 1:
        return False

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    if int(month) > 12 or int(month) < 1:
        return False
    if int(year) > 2070 or int(year) < 1900:
        return False
    return True


