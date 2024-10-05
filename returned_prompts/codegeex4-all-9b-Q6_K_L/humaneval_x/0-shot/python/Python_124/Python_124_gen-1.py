```python

def valid_date(date):
    import re
    date = date.strip()
    if re.match(r"^\d\d-\d\d-\d\d\d\d$", date):
        month, day, year = map(int, date.split('-'))
        if month > 0 and month < 13:
            if month in {1, 3, 5, 7, 8, 10, 12}:
                if day > 0 and day < 32:
                    return True
            elif month in {4, 6, 9, 11}:
                if day > 0 and day < 31:
                    return True
            elif month == 2:
                if day > 0 and day < 30:
                    return True
    return False
```
