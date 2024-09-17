def check_greater(arr: list, n: int) -> bool:
  return all(x > n for x in arr)