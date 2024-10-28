def change_date_format(date_string):
    """
    Args:
        date_string (str): date of format yyyy-mm-dd
    Returns:
        str: date of format dd-mm-yyyy
    """
    date_list = date_string.split('-')
    return f'{date_list[2]}-{date_list[1]}-{date_list[0]}'