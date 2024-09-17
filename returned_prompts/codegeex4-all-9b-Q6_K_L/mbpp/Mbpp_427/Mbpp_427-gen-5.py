def change_date_format(date_str):
    parts = date_str.split('-')
    return '-'.join([parts[2], parts[1], parts[0]])

