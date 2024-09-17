def check_monthnumb_number(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    elif month in [4, 6, 9, 11]:
        return False
    elif month == 2:
        return False
    else:
        return "Invalid month number"