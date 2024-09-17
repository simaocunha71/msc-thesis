def change_date_format(date: str) -> str:
  year, month, day = date.split("-")
  return f"{day}-{month}-{year}"