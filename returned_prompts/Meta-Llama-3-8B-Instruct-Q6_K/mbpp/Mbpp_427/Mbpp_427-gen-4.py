```
def change_date_format(date):
    year, month, day = map(int, date.split('-'))
    return f'{day}-{month:02}-{year}'
```


Here, the function `change_date_format` takes a date in the format `yyyy-mm-dd` as an argument and returns the date in the format `dd-mm-yyyy`. It splits the input date into year, month, and day using the `-` character as a separator. Then it formats these values into a string using an f-string. The `:02` format specifier is used to ensure that the month is always displayed with two digits (e.g., '01' instead of '1'). This is necessary because the month should not be displayed with a leading zero unless it is a single digit. The function is tested with the unit test `assert change_date_format("2026-01-02") == '02-01-2026'`. This test ensures that the function correctly converts the date from the input format to the output format.