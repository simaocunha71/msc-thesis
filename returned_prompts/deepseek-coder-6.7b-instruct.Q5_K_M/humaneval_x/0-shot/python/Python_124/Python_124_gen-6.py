
```python
import re

def valid_date(date):
    pattern = re.compile("^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$")
    if not re.match(pattern, date):
        return False
    m, d, y = map(int, date.split('-'))
    if m in (4, 6, 9, 11) and d > 30: return False
    if m == 2 and d > 29: return False
    return True
```

This solution uses a regular expression to check that the date string is in the correct format and that the numbers are within the correct range. It then splits the date string into its components and checks them separately.

A few notes about this solution:

1. The regular expression `^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$` checks for a date in the format mm-dd-yyyy.

2. The `|` symbol is a logical OR in regular expressions, so `(0[1-9]|1[0-2])` matches either a single digit from 1 to 9, or a two digit number from 10 to 12.

3. The `-` character matches itself in the regular expression, so it serves as the separator between the month, day, and year.

4. `[0-9]{4}` matches a four-digit year.

5. The `map(int, date.split('-'))` line splits the date string into its components and converts them to integers.

6. The `if m in (4, 6, 9, 11) and d > 30: return False` line checks if the month is one of the months with 30 days and if the day is more than 30.

7. The `if m == 2 and d > 29: return False` line checks if the month is February and if the day is more than 29.