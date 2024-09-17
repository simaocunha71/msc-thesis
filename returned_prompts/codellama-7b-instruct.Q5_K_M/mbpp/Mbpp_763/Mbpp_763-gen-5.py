
def find_min_diff(arr,n):
  minimum = 1000000
  for i in range(n-1):
    for j in range(i+1,n):
      if minimum > abs(arr[i] - arr[j]):
        minimum = abs(arr[i] - arr[j])
  return minimum


