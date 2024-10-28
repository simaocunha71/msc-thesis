def check_monthnumb_number(month):
    month_31_days = [1, 3, 5, 7, 8, 10, 12]
    if month in month_31_days:
        return True
    else:
        return False