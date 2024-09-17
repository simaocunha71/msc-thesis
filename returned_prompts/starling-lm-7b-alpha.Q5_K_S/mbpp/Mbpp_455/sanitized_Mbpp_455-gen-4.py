def check_monthnumb_number(month_num):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_num = int(month_num)
    if month_num in range(1,13):
        if months[month_num-1] in ['January', 'March', 'May', 'July', 'August', 'October', 'December', 'April', 'June', 'September', 'November']:
            return True
    return False