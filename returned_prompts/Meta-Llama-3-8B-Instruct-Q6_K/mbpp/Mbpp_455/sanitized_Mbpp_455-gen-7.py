def check_monthnumb_number(month_num):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_num <= 12 and month_num > 0 and month_days[month_num - 1] == 31