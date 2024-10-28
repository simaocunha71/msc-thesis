def is_majority(arr: list, n: int, element: int) -> bool:
  if n == 0:
    return False
  count = 0
  for i in range(n):
    if arr[i] == element:
      count += 1
  return count > n // 2