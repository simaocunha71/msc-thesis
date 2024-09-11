"""
def change_date_format(date):
    date_list = date.split('-')
    return date_list[1] + '-' + date_list[0] + '-' + date_list[2]

def test_change_date_format():
    assert change_date_format("2026-01-02") == '02-01-2026'

test_change_date_format()
"""

def change_date_format(date):
    date_list = date.split('-')
    return date_list[1] + '-' + date_list[0] + '-' + date_list[2]

def test_change_date_format():
    assert change_date_format("2026-01-02") == '02-01-2026'

test_change_date_format()

# Here is the Python3 code:
"""
def change_date_format(date):
    date_list = date.split('-')
    return date_list[1] + '-' + date_list[0] + '-' + date_list[2]

def test_change_date_format():
    assert change_date_format("2026-01-02") == '02-01-2026'

test_change_date_format()
"""

"""
Explanation:
The problem asks to convert a date string in yyyy-mm-dd format to dd-mm-yyyy format. We can achieve this by splitting the input string at the '-' delimiter and then re-arranging the parts to obtain the desired format.
In the provided solution, we define a function called `change_date_format` that takes a date string as an argument. Inside the function, we split the date string using the '-' delimiter and store the result in a list called `date_list`. We then concatenate the elements of `date_list` in the desired order to form the new date string in dd-mm-yyyy format.
To test the function, we define a test case using the `test_change_date_format` function. We assert