def odd_length_sum(arr: list) -> int:
  sum = 0
  for i in range(1,len(arr)):
    for j in range(i,len(arr)):
      if j-i+1%2:
        sum += arr[i-1]
  return sum