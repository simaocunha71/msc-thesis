def is_majority(arr, n, x):
  
  # get the first and last occurrence of the element
  first_occurrence = arr.index(x)
  last_occurrence = n - arr[::-1].index(x) - 1
  
  # check if element occurs more than n/2 times
  if last_occurrence - first_occurrence + 1 > n // 2:
    return True
  else:
    return False