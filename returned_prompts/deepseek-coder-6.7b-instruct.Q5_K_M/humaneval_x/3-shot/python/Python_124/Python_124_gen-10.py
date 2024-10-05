    import re
    match = re.search(r'(\d\d)-(\d\d)-(\d\d\d\d)', date)
    if match:
        month, day, year = map(int, match.groups())
        if 1 <= month <= 12:
            if month in (1, 3, 5, 7, 8, 10, 12):
                if 1 <= day <= 31:
                    return True
            elif month in (4, 6, 9, 11):
                if 1 <= day <= 30:
                    return True
            elif month == 2:
                if 1 <= day <= 29:
                    return True
    return False


