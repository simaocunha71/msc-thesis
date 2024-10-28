    import re

    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def is_valid_month(month):
        return 1 <= month <= 12

    def is_valid_day(day, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= day <= 31
        elif month in [4, 6, 9, 11]:
            return 1 <= day <= 30
        elif month == 2:
            return 1 <= day <= 29 if is_leap_year(year) else 1 <= day <= 28

    def is_valid_format(date):
        return re.match(r'\d{2}-\d{2}-\d{4}', date) is not None

    if not is_valid_format(date):
        return False

    month, day, year = map(int, date.split('-'))
    return is_valid_day(day, month, year) and is_valid_month(month)


