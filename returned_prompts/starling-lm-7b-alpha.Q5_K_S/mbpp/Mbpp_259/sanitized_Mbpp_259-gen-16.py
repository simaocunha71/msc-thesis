def maximize_elements(tup1: list,tup2: list) -> list:
  res = []
  for i in range(len(tup1)):
    if tup1[i] > tup2[i]:
      res.append(tup1[i])
    else:
      res.append(tup2[i])
  return tuple(res)