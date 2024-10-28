```
def change_date_format(date):
    return date[-2:] + '-' + date[5:7] + '-' + date[:4]
```


The problem is asking you to create a function that takes a date in the format "yyyy-mm-dd" and returns the same date in the format "dd-mm-yyyy". 

For example, if the input is "2026-01-02", the output should be "02-01-2026".

Here's a Python function that accomplishes this:

```
def change_date_format(date):
    return date[-2:] + '-' + date[5:7] + '-' + date[:4]
```

This function works by slicing the input string into three parts: the day, the month, and the year. It then concatenates these parts together in the correct order to form the output string. The `[-2:]` slice gets the last two characters of the string, which is the day. The `[5:7]` slice gets the characters starting from the 5th position and ending at the 7th position, which is the month. The `[:4]` slice gets the first four characters of the string, which is the year. 

The unit test `assert change_date_format("2026-01-02") == '02-01-2026'` ensures that the function works correctly.  It checks that the function returns the correct output for the input "2026-01-02". 

This function is case-insensitive, meaning it will work correctly even if the input string contains uppercase letters. It also assumes that the input string is in the correct format "yyyy-mm-dd". If the input string is not in this format, the function may not work correctly. 

In a real-world application, you might want to add error checking to handle invalid input dates. For example, you could check that the day is a valid number between 1 and 31, and that the month is a valid number between 1 and 12. You could also check that the year is a valid number. If any of these checks fail, you could raise an exception or return an error message. 