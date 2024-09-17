
def odd_length_sum(arr):
  total = 0
  n = len(arr)
  for i in range(n):
    total += ((i+1)*(n-i) + 1)//2 * arr[i]
  return total


