    def check_month_days(month, days):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return days >= 1 and days <= 31
        if month in [4, 6, 9, 11]:
            return days >= 1 and days <= 30
        if month == 2:
            if days == 29:
                return True
            return days >= 1 and days <= 28
        return False

    def check_date_format(date):
        try:
            date.index('-')
            return True
        except ValueError:
            return False

    def check_month_range(month):
        return month >= 1 and month <= 12

    month, days, year = [int(i) for i in date.split('-')]
    if not check_date_format(date):
        return False
    if not check_month_range(month):
        return False
    if not check_month_days(month, days):
        return False
    return True


