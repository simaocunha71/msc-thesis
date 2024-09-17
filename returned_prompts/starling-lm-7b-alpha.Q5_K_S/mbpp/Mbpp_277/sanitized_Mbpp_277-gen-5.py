def dict_filter(d,n):
  new_d = {}
  for key,value in d.items():
    if value >= n:
      new_d[key] = value
  return new_d