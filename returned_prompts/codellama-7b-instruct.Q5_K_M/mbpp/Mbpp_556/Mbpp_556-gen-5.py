
def find_Odd_Pair(arr: list, num: int) -> int:
  count = 0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if (arr[i]^arr[j])==num:
        count += 1
  return count


