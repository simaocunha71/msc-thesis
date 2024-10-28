def change_date_format(date):
    '''
    Convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
    '''
    parts = date.split('-')
    return parts[1] + '-' + parts[0] + '-' + parts[2]