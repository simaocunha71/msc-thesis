
def pancake_sort(lst):
  for i in range(len(lst)):
    m = max(0, len(lst)-i-1)
    lst[:m+1] = reversed(lst[:m+1])
    lst[m:] = sorted(lst[m:])
  return lst


