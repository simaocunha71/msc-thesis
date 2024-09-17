
def extract_values(string: str) -> list:
  values = []
  for i in string.split('"'):
    if i != '':
      values.append(i)
  return values


