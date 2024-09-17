```
def change_date_format(date):
    day, month, year = date.split('-')
    return f'{day}-{month}-{year}'
```


Here is the explanation:

The problem is asking to write a function that takes a date in the format "yyyy-mm-dd" and returns the same date in the format "dd-mm-yyyy".

We can solve this problem by splitting the input date string into day, month, and year using the '-' character as a delimiter. Then, we can return a new string with the day, month, and year in the desired format.

The unit test `assert change_date_format("2026-01-02") == '02-01-2026'` helps us to understand the problem better by providing an example of the expected output for a given input.

In the solution, we use Python's f-string formatting to create the new string with the day, month, and year in the desired format. The `f` before the string indicates that it's an f-string, and the `{day}-{month}-{year}` is a formatted string literal that replaces `{day}`, `{month}`, and `{year}` with the actual values of `day`, `month`, and `year`.