def check_monthnumber_number(month):
    if month in [1,3,5,7,8,10,12]:
        return False
    elif month in [4,6,9,11]:
        return True
    else:
        return True