
def find_Odd_Pair(lst: list,n: int) -> int:
  count = 0
  for i in range(n):
    for j in range(i+1, n):
      if lst[i]^lst[j] % 2 != 0:
        count += 1
  return count

