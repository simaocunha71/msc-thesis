def check_monthnumb_number(month):
    """
    Check if the given month number contains 31 days or not.
    """
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_index = months.index(month)
    if month_index in [0, 2, 4, 6, 7, 9, 11]:
        return True
    else:
        return False