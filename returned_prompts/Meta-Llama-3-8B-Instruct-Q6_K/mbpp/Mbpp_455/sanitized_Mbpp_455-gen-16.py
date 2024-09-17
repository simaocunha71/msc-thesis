def check_monthnumb_number(month_number):
    if 1<=month_number<=12:
        if month_number in [1,3,5,7,8,10,12]:
            return True
        else:
            return False
    else:
        return "Invalid month number"