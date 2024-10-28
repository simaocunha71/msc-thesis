def check_type(tup):
  if len(set(type(i) for i in tup)) == 1:
    return True
  else:
    return False