def sum_Of_Subarray_Prod(lst): 
  n = len(lst) 
  prod = [0]*n 
  subarrays = [0]*n 
  prod[0] = lst[0] 
  subarrays[0] = 1
  for i in range(1, n): 
    prod[i] = lst[i]*lst[i-1] 
    subarrays[i] = subarrays[i-1]*2+1
  return sum(prod)+sum(lst)