def change_date_format(date: str) -> str:
  y, m, d = date.split('-')
  return f"{d}-{m}-{y}"