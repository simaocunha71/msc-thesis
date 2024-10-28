def check_type(tup):
  return all(isinstance(ele, type(tup[0])) for ele in tup)