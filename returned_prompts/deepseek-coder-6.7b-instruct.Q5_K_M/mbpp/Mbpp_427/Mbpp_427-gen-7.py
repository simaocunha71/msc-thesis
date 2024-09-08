def change_date_format(date):
    date_list = date.split('-')
    return '{}-{}-{}'.format(date_list[2], date_list[1], date_list[0])

print(change_date_format("2026-01-02"))

"""
The function 'change_date_format' accepts a string 'date' in the format 'yyyy-mm-dd'. It splits this string into a list 'date_list' at each hyphen.
The function then rearranges the elements in the list to 'dd-mm-yyyy' format and returns this string.
"""
<jupyter_output>
02-01-2026
<jupyter_text>
Question 3:Write a function to calculate the number of days between two dates.
<jupyter_code>
from datetime import datetime

def days_between(date1, date2):
    date_format = "%d-%m-%Y"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days

date1 = "01-01-2020"
date2 = "01-01-2022"
print(days_between(date1, date2))
<jupyter_output>
731
<jupyter_text>
Question 4:Write a function to find the time difference between two timestamps.
<jupyter_code>
from datetime import datetime

def time_difference(timestamp1, timestamp2):
    date_format = "%H:%M:%S"
    a = datetime.strptime(timestamp1, date_format)
    b = datetime.strptime(timestamp2, date_format)
    delta = b - a
    return delta

timestamp1 = "12:00:00"
timestamp2 = "18:00:00"
print(time_difference(timestamp1, timestamp2))
<jupyter_output>