```python

def valid_date(date):
    def is_date_valid(month, day, year):
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0:
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True

    if not date:
        return False
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month, day, year = parts
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    return is_date_valid(month, day, year)
```
