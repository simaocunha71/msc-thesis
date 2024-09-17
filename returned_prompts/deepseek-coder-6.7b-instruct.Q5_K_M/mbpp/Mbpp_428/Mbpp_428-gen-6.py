
def shell_sort(lst):
  gap = len(lst) // 2
  while gap > 0:
    for i in range(gap, len(lst)):
      temp = lst[i]
      j = i
      while j >= gap and lst[j - gap] > temp:
        lst[j] = lst[j - gap]
        j = j-gap
      lst[j] = temp
    gap = gap // 2
  return lst


