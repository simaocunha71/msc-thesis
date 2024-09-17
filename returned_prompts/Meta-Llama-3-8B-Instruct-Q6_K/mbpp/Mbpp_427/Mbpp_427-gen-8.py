```
def change_date_format(date):
    year, month, day = date.split('-')
    return f'{day}-{month}-{year}'
```


In this function, we first split the input date string into year, month, and day. Then, we use f-string formatting to combine these parts in the desired format. The `assert` statement ensures that the function works correctly. For example, the input "2026-01-02" should produce the output "02-01-2026". 

This function assumes that the input date is in the correct format (yyyy-mm-dd). If the input date is in a different format, the function may not work correctly. 

For example, if the input date is "01-02-2026", the function will split it into year as "2026", month as "01-02", and day as an empty string. This will result in an incorrect output. To handle dates in different formats, you would need to add additional error checking and date parsing logic. 

For example, you could use the `datetime` module to parse the date string and then format it as needed. Here is an example:

```
from datetime import datetime

def change_date_format(date):
    dt = datetime.strptime(date, '%Y-%m-%d')
    return dt.strftime('%d-%m-%Y')
```

This function uses the `strptime` function to parse the input date string into a datetime object, and then the `strftime` function to format the datetime object as a string in the desired format. This approach is more robust and can handle dates in different formats.  However, it may be overkill for a simple date format conversion task.  The original function is simpler and may be sufficient for many use cases.  It depends on the specific requirements and constraints of your project.  Always consider the trade-offs between simplicity, robustness, and performance when designing and implementing your code.  In this case, the original function is simple and easy to understand, but it may not handle all possible input dates correctly.  The more robust function using the `datetime` module is more complex, but it can handle any valid date string in the input format.  It's up to you to decide which approach is best for your specific use case.  Always test your code thoroughly to ensure it works correctly in all the situations you expect it to.  In this case, you can test the function with a variety of input dates to make sure it produces the correct output