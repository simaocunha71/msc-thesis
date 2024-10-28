def check_element(lst,el):
  if all(x == el for x in lst):
    return True
  else:
    return False