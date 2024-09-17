
def sum_Of_Subarray_Prod(lst):
  n = len(lst)
  prod = [0]*n
  sum_prod = 0
  for i in range(n):
    prod[i] = lst[i] * (i+1) * (n-i)
    sum_prod += prod[i]
  return sum_prod


