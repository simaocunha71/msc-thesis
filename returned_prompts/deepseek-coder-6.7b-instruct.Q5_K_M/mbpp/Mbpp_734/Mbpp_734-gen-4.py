
def sum_Of_Subarray_Prod(lst):
  n = len(lst)
  prod = [0]*n
  prod[0] = lst[0]
  for i in range(1, n):
    prod[i] = lst[i]*lst[i-1]
  return sum(prod)


