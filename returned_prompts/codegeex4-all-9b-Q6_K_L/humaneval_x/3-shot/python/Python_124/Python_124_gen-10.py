    def is_valid(date):
        if len(date) != 10:
            return False
        if date[2] != '-' or date[5] != '-':
            return False
        if not date[:2].isdigit() or not date[3:5].isdigit() or not date[6:].isdigit():
            return False
        month, day, year = int(date[:2]), int(date[3:5]), int(date[6:])
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0 and day > 29:
                return False
            elif year % 4 != 0 and day > 28:
                return False
        return True

    return is_valid(date)