def check_monthnumb_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return True
    elif month_number in [4,6,9,11]:
        return False
    else:
        return True