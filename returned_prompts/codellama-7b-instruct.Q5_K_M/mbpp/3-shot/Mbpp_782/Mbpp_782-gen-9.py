
def odd_length_sum(arr):
  sum = 0
  for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
      if j-i+1 % 2 == 1:
        sum += arr[j] - arr[i]
  return sum


