def insert_element(lst, element):
  result = [element]
  for item in lst:
    result.append(element)
    result.append(item)
  return result