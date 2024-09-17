def change_date_format(date: str) -> str:
  date_list = date.split('-')
  return f'{date_list[2]}-{date_list[1]}-{date_list[0]}'