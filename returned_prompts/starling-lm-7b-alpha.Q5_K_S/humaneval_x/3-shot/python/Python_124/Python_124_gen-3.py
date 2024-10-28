    def check_month(month):
        return 1 <= month <= 12

    def check_day(month, day):
        if month == 2:
            return 1 <= day <= 29
        elif month in (1, 3, 5, 7, 8, 10, 12):
            return 1 <= day <= 31
        else:
            return 1 <= day <= 30

    def check_date(date_str):
        month, day, year = date_str.split('-')
        if month == '':
            return False
        if not check_month(month):
            return False
        if not check_day(month, day):
            return False
        return True

    return check_date(date)


