    try:
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)

        if year < 1 or month < 1 or month > 12 or day < 1:
            return False

        if month in [4, 6, 9, 11]:
            if day > 30:
                return False
        elif month == 2:
            if year % 4 == 0:
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        else:
            if day > 31:
                return False

        return True
    except:
        return False