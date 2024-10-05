    from datetime import datetime

    if len(date) != 10:
        return False

    if date[4] != '-' or date[7] != '-':
        return False

    day, month, year = map(int, date[3:5], date[0:2], date[6:10])

    if month < 1 or month > 12:
        return False

    if (month in [1, 3, 5, 7, 8, 10, 12] and day < 1 and day > 31) or \
       (month in [4, 6, 9, 11] and day < 1 and day > 30) or \
       (month == 2 and day < 1 and day > 29):
        return False

    try:
        datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        return False

    return True


