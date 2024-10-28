def pack_consecutive_duplicates(lst):
  result = [[i] for i in set(lst)]
  for i in lst:
    for j in result:
      if i == j[0]:
        j.append(i)
        break
  return result