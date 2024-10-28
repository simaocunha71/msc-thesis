def change_date_format(date):
  year, month, day = map(int, date.split('-'))
  return f"{day}-{month}-{year}"