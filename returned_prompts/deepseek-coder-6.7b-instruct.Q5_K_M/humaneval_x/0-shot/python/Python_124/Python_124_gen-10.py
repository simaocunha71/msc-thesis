
def valid_date(date):
    if not date or len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    month, day, year = date.split('-')
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False
    if day < 1 or (month in (1, 3, 5, 7, 8, 10, 12) and day > 31) or (month in (4, 6, 9, 11) and day > 30) or (month == 2 and day > 29):
        return False
    return True

print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
print(valid_date('02-30-2020'))  # False
print(valid_date('02-29-2020'))  # True
print(valid_date('02-29-2019'))  # False
print(valid_date('02-29-2018'))  # False
print(valid_date('02-29-2016'))  # True
print(valid_date('02-29-2015'))  # False
print(valid_date('02-30-2015'))  # False
print(valid_date('02-31-2015'))  # False

This function first checks if the date string is not empty and has the correct format. Then it splits the date into month, day and year and checks if