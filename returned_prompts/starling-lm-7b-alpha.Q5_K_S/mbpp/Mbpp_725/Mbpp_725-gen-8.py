
def extract_quotation(string: str) -> list:
  result = []
  index = 0
  while index < len(string):
    if string[index] == '"':
      index += 1
      while string[index] != '"':
        result.append(string[index])
        index += 1
      index += 1
  return result


