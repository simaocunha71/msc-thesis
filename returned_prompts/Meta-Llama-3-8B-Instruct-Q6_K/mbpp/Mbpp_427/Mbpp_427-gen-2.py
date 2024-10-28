```
def change_date_format(date):
    year, month, day = date.split('-')
    return f'{day}-{month}-{year}'
```



This function takes a date string in the format "yyyy-mm-dd" and returns a new string in the format "dd-mm-yyyy". It does this by splitting the input string into its year, month, and day components, and then reassembling them in the desired order. The unit test `assert change_date_format("2026-01-02") == '02-01-2026'` ensures that the function works correctly for at least one example input. 

Note that this function assumes that the input date string is in the correct format. If the input date string is not in the correct format, the function may not work correctly. In a real-world application, you might want to add error checking code to handle this situation.  For example, you could use the `datetime` module to parse the input date string, like this:

```
import datetime

def change_date_format(date):
    try:
        dt = datetime.datetime.strptime(date, '%Y-%m-%d')
        return dt.strftime('%d-%m-%Y')
    except ValueError:
        return "Invalid date format"
```

This version of the function uses the `strptime` method to parse the input date string, and the `strftime` method to format the resulting `datetime` object as a string in the desired format. If the input date string is not in the correct format, the `strptime` method will raise a `ValueError` exception, which is caught by the `except` block and replaced with an error message.  This makes the function more robust and easier to use.  For example, if you call the function with an invalid input date string, like this:

```
print(change_date_format("2026-13-02"))
```

The function will print the error message "Invalid date format" instead of raising an exception.  This makes it easier to handle errors and provides a more user-friendly interface.  However, in a real-world application, you would probably want to handle errors in a more sophisticated way, such as by displaying an error message to the user or logging the error to a file.  The `except` block in this example is just a simple way to demonstrate how you could handle errors in a basic way.  In a real-world application, you would probably want to add more sophisticated error handling code to make the function more robust and