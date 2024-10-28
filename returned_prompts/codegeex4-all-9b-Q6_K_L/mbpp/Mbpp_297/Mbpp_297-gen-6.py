def flatten_list(lst: list) -> list:
  res = []
  for el in lst:
    if isinstance(el, list):
      res.extend(flatten_list(el))
    else:
      res.append(el)
  return res

