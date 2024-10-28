
def valid_date(date):
    if date == "":
        return False
    date_parts = date.split("-")
    if len(date_parts) != 3:
        return False
    month, day, year = date_parts
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        if day == 29 and year % 4 != 0:
            return False
    if day == 31 and month in [1, 3, 5, 7, 8, 10, 12]:
        return False
    return True

print(valid_date('03-11-2000')) # True
print(valid_date('15-01-2012')) # False
print(valid_date('04-0-2040')) # False
print(valid_date('06-04-2020')) # True
print(valid_date('06/04/2020')) # False
print(valid_date('02-30-2020')) # False
print(valid_date('02-29-2020')) # True
print(valid_date('02-29-2019')) # False
print(valid_date('02-29-2016')) # True
print(valid_date('02-30-2019')) # False

This code first checks if the date string is empty or if it doesn't have the correct format. It then checks if the month, day, and year are all numeric and within the expected ranges. It also checks for special cases like February 29, and February 30 in non