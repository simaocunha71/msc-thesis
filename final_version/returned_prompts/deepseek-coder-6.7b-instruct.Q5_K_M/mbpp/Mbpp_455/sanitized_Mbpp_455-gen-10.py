def check_monthnumb_number(n):
    month_with_31_days = [1,3,5,7,8,10,12]
    if n in month_with_31_days:
        return True
    else:
        return False