def change_date_format(date):
    day, month, year = date.split('-')
    return f'{day}-{month}-{year}'