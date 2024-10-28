def valid_date(date):
    # check if date string is not empty
    if not date:
        return False

    # check if date is in the format mm-dd-yyyy
    if '-' not in date or len(date.split('-')) != 3:
        return False

    # split date string into month, day, year
    month, day, year = date.split('-')

    # check if month, day, year are integers
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    # convert month, day, year to integers
    month, day, year = int(month), int(day), int(year)

    # check if month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # check if day is between 1 and 31 for months 1, 3, 5, 7, 8, 10, 12
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False

    # check if day is between 1 and 30 for months 4, 6, 9, 11
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False

    # check if day is between 1 and 29 for the month 2
    if month == 2 and (day < 1 or day > 29):
        return False

    # if all checks pass, return True
    return True