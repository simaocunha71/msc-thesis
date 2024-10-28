def pancake_sort(lst):
  n = len(lst)
  for i in range(n-1, 0, -1):
    max_index = i
    for j in range(i):
      if lst[j] > lst[max_index]:
        max_index = j
    if max_index != i:
      lst[max_index], lst[i] = lst[i], lst[max_index]
      lst[:max_index+1] = lst[:max_index+1][::-1]
  return lst

