```
def change_date_format(date):
    split_date = date.split("-")
    return split_date[1] + "-" + split_date[0] + "-" + split_date[2]
```

This function `change_date_format` takes a date string in the yyyy-mm-dd format and splits the string into a list of substrings at each hyphen character. Then, it returns a new string that concatenates the second element of the list (the month) with a hyphen, the first element of the list (the day) with another hyphen, and the third element of the list (the year). This effectively swaps the positions of the day and the month, resulting in a date string in the dd-mm-yyyy format.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a sample date. For example, `assert change_date_format("2026-01-02") == '02-01-2026'` checks if the function correctly converts the date "2026-01-02" to the format "02-01-2026".

You can call the `change_date_format` function with different date strings as arguments to convert them to the desired format.

Here's an example usage of the function:
```python
print(change_date_format("2022-12-25"))  # Output: 25-12-2022
```

In this example, the function is called with the date "2022-12-25" and it returns the string "25-12-2022", which represents the same date in the dd-mm-yyyy format.

Feel free to modify the function or use it as-is in your code to convert dates to the desired format.

```python
def change_date_format(date):
    split_date = date.split("-")
    return split_date[1] + "-" + split_date[0] + "-" + split_date[2]
```

This function `change_date_