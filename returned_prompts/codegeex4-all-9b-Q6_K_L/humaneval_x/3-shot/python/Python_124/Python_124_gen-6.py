    # check if the date is not empty
    if not date:
        return False

    # check if the date is in the format: mm-dd-yyyy
    if len(date.split('-')) != 3:
        return False

    # check if the number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    month, day, year = date.split('-')
    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False
    elif month == 2:
        if day > 29:
            return False

    return True