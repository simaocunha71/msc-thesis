def change_date_format(date_string: str) -> str:
  year, month, day = date_string.split("-")
  return f"{day}-{month}-{year}"