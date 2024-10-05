    def get_days_in_month(month: int, year: int) -> int:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return 29
            else:
                return 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30

    month, day, year = map(int, date.split('-'))

    if not date or len(date.split('-')) != 3:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > get_days_in_month(month, year):
        return False
    return True


