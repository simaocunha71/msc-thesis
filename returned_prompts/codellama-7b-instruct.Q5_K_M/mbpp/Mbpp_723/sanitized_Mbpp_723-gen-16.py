def count_same_pair(list_a,list_b):
  count = 0
  for i in range(len(list_a)):
    if list_a[i] == list_b[i]:
      count += 1
  return count