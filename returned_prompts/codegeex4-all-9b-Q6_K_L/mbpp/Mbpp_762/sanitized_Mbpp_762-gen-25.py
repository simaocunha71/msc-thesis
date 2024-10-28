def check_monthnumber_number(month_number):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_number >= 1 and month_number <= 12:
        return days_in_month[month_number-1] == 30
    else:
        return False