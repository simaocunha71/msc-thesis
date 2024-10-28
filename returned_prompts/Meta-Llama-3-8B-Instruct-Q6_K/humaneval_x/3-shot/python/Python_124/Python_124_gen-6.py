    def validate_date(date):
        if date == '':
            return False
        date_list = date.split('-')
        if len(date_list) != 3:
            return False
        month, day, year = date_list
        if not month.isdigit() or not day.isdigit() or not year.isdigit():
            return False
        month = int(month)
        day = int(day)
        year = int(year)
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month == 2:
            if day < 1 or day > 29:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        return True
    return validate_date(date)  # replace date with your input date string


