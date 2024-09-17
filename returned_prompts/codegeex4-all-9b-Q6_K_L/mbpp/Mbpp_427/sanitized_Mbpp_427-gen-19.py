def change_date_format(date: str) -> str:
  year, month, day = map(int, date.split('-'))
  return f'{day}-{month}-{year}'