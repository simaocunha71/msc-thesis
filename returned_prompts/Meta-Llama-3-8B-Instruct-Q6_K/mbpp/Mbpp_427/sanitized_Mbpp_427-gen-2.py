def change_date_format(date_str):
    day, month, year = date_str.split('-')
    return f'{day}-{month}-{year}'