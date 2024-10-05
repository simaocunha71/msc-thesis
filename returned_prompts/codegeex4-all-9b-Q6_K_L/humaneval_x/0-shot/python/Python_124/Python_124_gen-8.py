def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split('-')

    # Check if the date is in the correct format
    if len(month) != 2 or len(day) != 2 or len(year) != 4 or '-' not in date:
        return False

    # Check if the year is a valid number
    if not year.isdigit() or int(year) < 1 or int(year) > 9999:
        return False

    # Check if the month is a valid number
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return False

    # Check if the day is a valid number
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        return False

    # Check if the day is valid for the given month
    if (int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) > 31) or \
       (int(month) in [4, 6, 9, 11] and int(day) > 30) or \
       (int(month) == 2 and int(day) > 29):
        return False

    return True