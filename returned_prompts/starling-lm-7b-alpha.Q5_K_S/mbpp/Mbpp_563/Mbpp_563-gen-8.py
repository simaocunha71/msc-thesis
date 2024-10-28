
def extract_values(string: str) -> list:
  values = string.split('"')
  values = values[1::2]
  return values


