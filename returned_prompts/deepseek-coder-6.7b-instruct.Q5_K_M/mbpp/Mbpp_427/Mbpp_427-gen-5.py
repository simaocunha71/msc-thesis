
def change_date_format(date: str) -> str:
  date_parts = date.split('-')
  return '{}-{}-{}'.format(date_parts[2], date_parts[1], date_parts[0])


