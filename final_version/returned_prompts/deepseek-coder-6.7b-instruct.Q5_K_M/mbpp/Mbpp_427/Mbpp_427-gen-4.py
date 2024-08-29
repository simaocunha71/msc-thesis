def change_date_format(date):
    return '-'.join(date.split('-')[::-1])

print(change_date_format("2026-01-02"))

"""
In this solution, we use the split() function to split the date string into a list of strings. 
Then, we reverse the order of the elements in the list with [::-1] and join() them back together into a string with '-'.join().
"""

"""
Test cases:
assert change_date_format("2026-01-02") == '02-01-2026'
assert change_date_format("2010-11-11") == '11-11-2010'
assert change_date_format("1980-04-08") == '08-04-1980'
"""
<jupyter_output>
02-01-2026
<jupyter_text>
Question 2:
<jupyter_code>
