
def extract_quotation(string:str):
  result = []
  start = False
  end = False
  for c in string:
    if c == '"':
      if start:
        result.append(c)
      end = True
      start = False
    elif end and c != " ":
      result.append(c)
    elif not start and c != " ":
      start = True
  return result[1:len(result)-1].split('"')


