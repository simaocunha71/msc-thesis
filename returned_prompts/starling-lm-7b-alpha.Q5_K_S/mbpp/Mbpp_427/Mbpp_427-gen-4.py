```
def change_date_format(date_string):
    date_list = date_string.split("-")
    return '{}-{}-{}'.format(date_list[2], date_list[1], date_list[0])
```

Explanation:

The function `change_date_format` takes a string `date_string` as an input. This string is split into a list using the `split` method, with the delimiter being the dash "-". This will create a list with three elements, representing the year, month, and day of the date.

The function then uses the `format` method to create a new string with the format 'dd-mm-yyyy'. The `date_list[2]` represents the day, `date_list[1]` represents the month, and `date_list[0]` represents the year. The new string is returned as the result of the function.

To test the function, the assert statement is used to verify that the function correctly converts the date string "2026-01-02" to the desired format of "02-01-2026".

Overall, this function allows you to convert a date from the yyyy-mm-dd format to the dd-mm-yyyy format.

Here's an example of how to use the function:
```python
date_string = "2026-01-02"
result = change_date_format(date_string)
print(result)  # Output: 02-01-2026
```

In this example, the `change_date_format` function is called with the date string "2026-01-02". The returned result is stored in the variable `result`, and then printed to the console. The output will be "02-01-2026", which is the date string in the desired format.

It's important to note that the `split` method used in this solution is case-sensitive. If the input date string has a different format (e.g., "2026/01/02"), the function will not produce the correct result.

To make the function more robust and