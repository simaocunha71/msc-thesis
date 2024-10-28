
def odd_length_sum(arr):
  sum_of_odd_length = 0
  for i in range(1,len(arr)):
    for j in range(i+1, len(arr)):
      if j-i+1 % 2 != 0:
        sum_of_odd_length += arr[j] - arr[i-1]
  return sum_of_odd_length


