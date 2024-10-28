def check_min_heap(lst):
  n = len(lst) 
  for i in range(int(n/2)-1):
    if lst[i]>lst[2*i+1]:
      return False
    if 2*i+2<n:
      if lst[i]>lst[2*i+2]:
        return False
  return True