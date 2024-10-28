def comb_sort(lst: list) -> list:
  gap = len(lst)
  while gap > 1:
    gap = (gap * 10) // 13
    for i in range(gap, len(lst)):
      j = i
      while j >= gap and lst[j-gap] > lst[j]:
        lst[j], lst[j-gap] = lst[j-gap], lst[j]
        j -= gap
  return lst