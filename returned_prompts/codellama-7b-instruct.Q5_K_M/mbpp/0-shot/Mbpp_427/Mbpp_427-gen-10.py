def change_date_format(date):
    """
    Change a date in the format yyyy-mm-dd to dd-mm-yyyy
    """
    return "-".join(reversed(date.split("-")))
