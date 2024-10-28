
def valid_date(date):
    # Split the date
    month, day, year = map(int, date.split('-'))
    # Check if the date is not empty
    if not date:
        return False
    # Check if the date is in the correct format
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    # Check if the year is not in the 20th or 21st century
    if year < 1900 or year > 2100:
        return False
    # Check if the month is not less than 1 or higher than 12
    if month < 1 or month > 12:
        return False
    # Check if the number of days is valid for the given month and year
    if month in [2,4,6,9,11]:
        if day < 1 or day > 30:
            return False
    elif month in [1,3,5,7,8,10,12]:
        if day < 1 or day > 31:
            return False
    elif month == 2:
        if day < 1 or day > 28 or (day == 29 and not is_leap_year(year)):
            return False
    # If all the conditions are satisfied, the date is valid
    return True

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


valid_date('03-11-2000') # True
valid_date('15-01-2012') # False
valid_date('04-0-2040') # False
valid_date('06-04-2020') # True
valid_date('06/04/2020') # False

























