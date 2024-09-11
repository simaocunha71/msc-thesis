def check_element(lst, element):
  return all(x == element for x in lst) if len(set(lst)) == 1 else False