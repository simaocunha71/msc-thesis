
def valid_date(date):
    if date == '':
        return False
    if date.count('-') != 2:
        return False
    parts = date.split('-')
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
    if month == 2 and day > 29:
        return False
    if month not in [1, 3, 5, 7, 8, 10, 12] and day > 30:
        return False
    if year < 1:
        return False
    return True

print(valid_date('03-11-2000')) # True

print(valid_date('15-01-2012')) # False

print(valid_date('04-0-2040')) # False

print(valid_date('06-04-2020')) # True

print(valid_date('06/04/2020')) # False
print(valid_date('')) # False
print(valid_date('03-04-2015')) # True
print(valid_date('02-30-2020')) # False
print(valid_date('02-29-2020')) # True
print(valid_date('12-31-2020')) # True
print(valid_date('02-29-2019')) # False
print(valid_date('02-30-2019')) # False
print(valid_date('06-40-2020')) # False
print(valid_date('1