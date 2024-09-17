
def extract_quotation(s: str) -> list:
  result = []
  s = s.replace('"', '')
  for i in s.split():
    result.append(i)
  return result


