
def valid_date(date):
    if len(date) == 0:
        return False
    else:
        month, day, year = date.split('-')
        if month.isdigit() and day.isdigit() and year.isdigit():
            if (int(month) > 0 and int(month) <= 12 and int(day) > 0 and int(day) <= 31 and int(year) > 0 and int(year) <= 9999):
                if (month != '02' or day != '30'):
                    if (month != '02' or day != '31'):
                        if (month != '02' or day != '32'):
                            if (month == '02' and int(day) <= 28):
                                if (month == '02' and int(day) <= 29):
                                    if (month == '02' and int(day) <= 30):
                                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


# Another solution:

def valid_date(date):
    if len(date) == 0:
        return False
    try:
        month, day, year = [int(i) for i in date.split('-')]
    except ValueError:
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month in [4, 6, 9, 11] else 29 if month == 2 else day):
        return False
    if not (1 <= year <= 9999):
        return False
    return True

# Testing the function with some inputs
print(valid_date('03-11-2000'))  # Expected output: True
print(valid_date('15-01-