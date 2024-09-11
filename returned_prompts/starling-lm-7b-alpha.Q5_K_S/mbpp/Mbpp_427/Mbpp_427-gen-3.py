```
def change_date_format(date):
    return date.split('-')[2] + '-' + date.split('-')[1] + '-' + date.split('-')[0]
```

Explanation:
The function `change_date_format` takes a date string in the format `yyyy-mm-dd` as input. It splits the string using the `-` delimiter to create a list of three elements: the year, month, and day. The function then concatenates the day, month, and year elements in the desired format, separated by `-`, and returns the result.

The `assert` statement is used to verify that the function correctly converts the date from `2026-01-02` to `'02-01-2026'`. By comparing the expected output with the actual output of the function, we can ensure that the function is working correctly.

To use the function, you can simply call it with a date string in the `yyyy-mm-dd` format, and it will return the converted date in the `dd-mm-yyyy` format.

For example, if you call `change_date_format("2026-01-02")`, it will return `'02-01-2026'`.

Note that the function assumes the input date string is always in the `yyyy-mm-dd` format, and does not perform any error checking or validation. It is important to ensure that the input date string is in the correct format before passing it to the function.

Overall, the provided solution is a simple and efficient way to convert a date from the `yyyy-mm-dd` format to the `dd-mm-yyyy` format using Python.

Here are some additional test cases to further validate the function:

```python
def test_change_date_format():
    assert change_date_format("2021-09-15") == '15-09-2021'
    assert change_date_format("2019-03-31") == '31-03-2019'
    assert change_date_format("202