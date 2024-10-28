def is_majority(arr: list, n: int, elem: int) -> bool:
  if arr.count(elem) > n // 2:
    return True
  return False