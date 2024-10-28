def odd_length_sum(arr):
  sum=0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if j-i+1 % 2 != 0:
        sum+=arr[j]
  return sum