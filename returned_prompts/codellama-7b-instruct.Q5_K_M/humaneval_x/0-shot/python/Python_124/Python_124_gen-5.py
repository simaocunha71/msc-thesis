
import re

def valid_date(date):
    if not date:
        return False

    if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
        return False

    month, day, year = date.split('-')

    if month == '02':
        if int(day) not in range(1, 29):
            return False
    elif int(day) not in range(1, 31):
        return False

    if int(month) not in range(1, 13):
        return False

    return True


