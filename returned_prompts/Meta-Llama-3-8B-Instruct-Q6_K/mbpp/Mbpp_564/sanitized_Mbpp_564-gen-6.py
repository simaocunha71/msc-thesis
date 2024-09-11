def count_Pairs(lst, k):
  if k <= 0:
    return 0
  count = 0
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      if lst[i] != lst[j]:
        count += 1
  return count