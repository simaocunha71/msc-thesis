def get_equal(tup_list):
  if len(set(len(t) for t in tup_list)) == 1:
    return True
  else:
    return False