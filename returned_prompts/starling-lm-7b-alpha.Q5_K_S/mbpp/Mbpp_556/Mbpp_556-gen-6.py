
def find_Odd_Pair(arr, x):
  res = 0
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if ((arr[i] ^ arr[j]) & 1) == 1:
        res += 1
  return res


