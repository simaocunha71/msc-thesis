
import re

def valid_date(date):
    pattern = r"(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d"
    if date == '':
        return False
    elif not re.match(pattern, date):
        return False
    else:
        month, day, year = date.split("-")
        if month == '02' and day > 29:
            return False
        if int(month) in [4,6,9,11] and int(day) > 30:
            return False
        if int(month) in [1,3,5,7,8,10,12] and int(day) > 31:
            return False
        if int(month) > 12 or int(month) < 1:
            return False
        if int(day) > 31 or int(day) < 1:
            return False
        if int(year) > 2020 or int(year) < 1900:
            return False
        return True

# Tests

assert valid_date('03-11-2000') == True
assert valid_date('15-01-2012') == False
assert valid_date('04-0-2040') == False
assert valid_date('06-04-2020') == True
assert valid_date('06/04/2020') == False
assert valid_date('') == False
assert valid_date('13-01-2012') == False
assert valid_date('02-29-2000') == True
assert valid_date('02-29-2001') == False
assert valid_date('02-29-2010') == False
assert valid_date('02-29-2020') == True
assert valid_date('02-29-2021') == False
assert valid