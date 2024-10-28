
def sum_Of_Subarray_Prod(arr):
  n = len(arr)
  result = 0
  for i in range(n):
    for j in range(i, n):
      temp = 1
      for k in range(i, j+1):
        temp *= arr[k]
      result += temp
  return result


