def insert_element(lst, element):
  result = []
  for i in lst:
    result.extend([element, i])
  return result

