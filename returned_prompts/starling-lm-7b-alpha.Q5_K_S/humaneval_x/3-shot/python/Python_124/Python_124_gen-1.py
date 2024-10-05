    def is_valid_day(month, day):
        if month in [2, 4, 6, 9, 11]:
            return 1 <= day <= 30
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= day <= 31
        else:
            return 1 <= day <= 29  # Assume that the year is not a leap year

    def is_valid_month(month):
        return 1 <= month <= 12

    def is_valid_date(date):
        month, day, year = date.split('-')
        return is_valid_month(month) and is_valid_day(month, day)

    return is_valid_date(date)


