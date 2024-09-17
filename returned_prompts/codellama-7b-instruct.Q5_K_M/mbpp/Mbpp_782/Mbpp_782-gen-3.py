
def odd_length_sum(arr):
  sum = 0
  for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
      sum += arr[i] + arr[j]
  return sum


