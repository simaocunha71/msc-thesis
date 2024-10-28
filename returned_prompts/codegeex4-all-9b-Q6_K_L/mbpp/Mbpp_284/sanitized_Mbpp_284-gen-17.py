def check_element(lst,element):
  if all(i == element for i in lst):
    return True
  else:
    return False