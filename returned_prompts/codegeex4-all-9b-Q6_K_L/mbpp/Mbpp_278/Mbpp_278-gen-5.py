def count_first_elements(tup):
  count=0
  for i in tup:
    if type(i) is not tuple:
      count+=1
    else:
      break
  return count