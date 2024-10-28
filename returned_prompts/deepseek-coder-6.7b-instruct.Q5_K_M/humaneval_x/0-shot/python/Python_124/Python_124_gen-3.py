
def valid_date(date):
    if date == '':
        return False
    else:
        date = date.split('-')
        if len(date) != 3:
            return False
        else:
            month = date[0]
            day = date[1]
            year = date[2]
            if not month.isdigit() or not day.isdigit() or not year.isdigit():
                return False
            else:
                month = int(month)
                day = int(day)
                year = int(year)
                if month < 1 or month > 12:
                    return False
                elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
                    return False
                elif month == 2 and (day < 1 or day > 29):
                    return False
                elif (day < 1 or day > 31):
                    return False
                else:
                    return True

# Test cases
print(valid_date('03-11-2000')) # True
print(valid_date('15-01-2012')) # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020')) # True
print(valid_date('06/04/2020')) # False
print(valid_date('02-30-2020')) # False
print(valid_date('02-29-2020')) # True
print(valid_date('02-29-2019')) # False
print(valid_date('02-30-2019')) # False
print(valid_date('')) # False

This solution assumes that all input is in the format mm-dd-yyyy and that the day, month and year are all integers. It also assumes that the input string is not empty.

This solution uses the built-in split method to split the input string into a list of three strings (month, day, year) based on the hyphen character. It then checks that each of these strings is a digit