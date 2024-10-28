def check_monthnumber_number(number):
    months_with_30_days = [4, 6, 9, 11]
    if number in months_with_30_days:
        return True
    else:
        return False