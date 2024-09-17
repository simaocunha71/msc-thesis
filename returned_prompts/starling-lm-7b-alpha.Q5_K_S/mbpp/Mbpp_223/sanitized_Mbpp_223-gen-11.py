def is_majority(arr: list, n: int, elem: int) -> bool:
  count = 0
  for i in range(len(arr)):
    if arr[i] == elem:
      count += 1
    if count > n//2:
      return True
  return False