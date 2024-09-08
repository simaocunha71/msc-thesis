from datetime import datetime

def date_difference(day1, month1, year1, day2, month2, year2):
    date1 = datetime(year1, month1, day1)
    date2 = datetime(year2, month2, day2)
    difference = date2 - date1
    return difference.days

print(date_difference(1, 1, 2020, 1, 1, 2021)) # 366

"""
Write a function to find the next date of a given date.
