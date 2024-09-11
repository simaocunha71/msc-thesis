def change_date_format(date):
  year = date[0:4]
  month = date[5:7]
  day = date[8:10]
  return f'{day}-{month}-{year}'