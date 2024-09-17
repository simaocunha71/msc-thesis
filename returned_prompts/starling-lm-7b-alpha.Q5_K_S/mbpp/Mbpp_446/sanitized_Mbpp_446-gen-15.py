def count_Occurrence(tup, li):
  count = 0
  for i in li:
    for j in tup:
      if i == j:
        count += 1
  return count