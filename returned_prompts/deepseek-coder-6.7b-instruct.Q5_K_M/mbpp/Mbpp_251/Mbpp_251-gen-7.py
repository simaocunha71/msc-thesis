
def insert_element(lst, elem):
  res = []
  for i in lst:
    res.extend([elem, i])
  return res[:-1]


