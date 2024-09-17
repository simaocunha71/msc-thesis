def is_majority(arr: list, n: int, elem: int) -> bool:
  cnt = 0
  for i in range(n):
    if arr[i] == elem:
      cnt += 1
  return cnt > n//2