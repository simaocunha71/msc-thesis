def change_date_format(date_str):
    year, month, day = map(int, date_str.split('-'))
    return f'{day}-{month:02d}-{year}'