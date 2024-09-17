def comb_sort(lst):
  gap = len(lst)
  shrink = 1.3
  sorted = False
  while not sorted:
    gap = max(1, int(gap/shrink))
    if gap > 1:
      sorted = False
    else:
      sorted = True
    i = 0
    while i + gap < len(lst):
      if lst[i] > lst[i+gap]:
        lst[i], lst[i+gap] = lst[i+gap], lst[i]
        sorted = False
      i += 1
  return lst