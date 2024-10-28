    import re

    def is_valid_date(date):
        if not re.match(r'\d{2}-\d{2}-\d{4}', date):
            return False

        month, day, year = map(int, date.split('-'))

        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        if month in [4, 6, 9, 11] and day > 30:
            return False

        if month == 2:
            if year % 4 == 0 and day > 29:
                return False
            elif day > 28:
                return False

        return True

    return is_valid_date(date)