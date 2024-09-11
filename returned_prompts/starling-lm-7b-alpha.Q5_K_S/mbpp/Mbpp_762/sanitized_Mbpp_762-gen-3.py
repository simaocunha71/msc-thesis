def check_monthnumber_number(month):
    if month == 2:
        return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return False
    else:
        return True