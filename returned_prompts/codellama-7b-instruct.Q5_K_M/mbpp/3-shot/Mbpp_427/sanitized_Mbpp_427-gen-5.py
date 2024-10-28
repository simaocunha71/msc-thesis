def change_date_format(date: str) -> str:
    day, month, year = date.split('-')
    return f'{day}-{month}-{year}'