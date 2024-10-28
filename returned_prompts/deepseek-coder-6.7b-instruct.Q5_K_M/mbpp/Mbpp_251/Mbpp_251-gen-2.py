
def insert_element(lst, element):
  return [element for i in lst for element in (i, element)]


