def count_Occurrence(tup,lis):
  count = 0
  for i in lis:
    for j in tup:
      if j == i:
        count += 1
  return count