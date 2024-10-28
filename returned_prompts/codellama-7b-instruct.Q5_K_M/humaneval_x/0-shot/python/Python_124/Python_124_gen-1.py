
def valid_date(date):
    if date == '':
        return False
    else:
        date_parts = date.split('-')
        day = int(date_parts[1])
        month = int(date_parts[0])
        year = int(date_parts[2])
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month == 2:
            if day < 1 or day > 29:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        return True


