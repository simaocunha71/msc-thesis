```
def change_date_format(date):
    return date[-2:] + '-' + date[5:7] + '-' + date[:4]
``` 

The unit test `assert change_date_format("2026-01-02") == '02-01-2026'` helps to understand the problem better. It shows that the function should take a date in the format 'yyyy-mm-dd' and return the same date in the format 'dd-mm-yyyy'.

In the function, we are slicing the input string to get the day, month and year parts. We are using the index positions to get the day (last two characters), month (5th and 6th characters) and year (first four characters). Then we are concatenating these parts with '-' in between to form the output string. 