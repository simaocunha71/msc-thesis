def change_date_format(date_str):
    year, month, day = date_str.split('-')
    return f'{day}-{month}-{year}'