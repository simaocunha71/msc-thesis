    def check_day(month, day):
        if month == 2 and day > 29:
            return False
        elif 1 <= month <= 12 and 1 <= day <= 31:
            return True
        elif 1 <= month <= 12 and 1 <= day <= 30:
            return True
        else:
            return False

    def check_month(month):
        if 1 <= month <= 12:
            return True
        else:
            return False

    month, day, year = date.split('-')
    month, day = int(month), int(day)

    if len(date) != 10 or not check_month(month) or not check_day(month, day):
        return False
    else:
        return True


