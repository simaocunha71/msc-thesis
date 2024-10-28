
from itertools import combinations
def sum_Of_Subarray_Prod(arr):
  prod = 0
  for i in range(1, len(arr)+1):
    for subset in combinations(arr, i):
      prod += prod_of_list(list(subset))
  return prod

def prod_of_list(lst):
  prod = 1
  for num in lst:
    prod *= num
  return prod


