
def comb_sort(lst: list):
  gap = len(lst)
  swapped = True
  while gap > 1 or swapped:
    gap = int(gap / 1.247330950103979)
    if gap < 1:
      gap = 1
    swapped = False
    for i in range(len(lst) - gap):
      if lst[i] < lst[i + gap]:
        lst[i], lst[i + gap] = lst[i + gap], lst[i]
        swapped = True
  return lst

