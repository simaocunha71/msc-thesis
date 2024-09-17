def check_monthnumber_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return False
    elif month_number == 2:
        return False
    else:
        return True