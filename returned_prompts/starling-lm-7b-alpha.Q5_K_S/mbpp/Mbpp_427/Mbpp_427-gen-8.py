```
def change_date_format(date):
    return date.split('-')[2]+'-'+date.split('-')[1]+'-'+date.split('-')[0]
```

Explanation:

The function `change_date_format` takes a string `date` in the format of `yyyy-mm-dd` and uses the built-in `split` function to split the string into three parts using the hyphen as the separator. Then, it concatenates the three parts in the desired order to create a new string in the format `dd-mm-yyyy`.

To test the function, you can use the `assert` statement to check if the returned value of `change_date_format("2026-01-02")` is equal to the expected output `'02-01-2026'`.

The `split` function splits a string at the specified separator and returns a list of the separated substrings. In this case, it splits the `date` string at each hyphen ('-') and returns a list with three elements: the year, the month, and the day.

By using string concatenation (`+` operator), the function creates a new string with the day, month, and year in the desired format: `dd-mm-yyyy`.

Overall, this function provides a simple and efficient way to convert a date from `yyyy-mm-dd` format to `dd-mm-yyyy` format.

```python
def change_date_format(date):
    return date.split('-')[2]+'-'+date.split('-')[1]+'-'+date.split('-')[0]

print(change_date_format("2026-01-02"))  # Output: '02-01-2026'
```

This code demonstrates the usage of the `change_date_format` function with the example input `"2026-01-02"`. The function returns the desired output `'02-01-2026'`, which is then printed to the console.
```

```python
```python
