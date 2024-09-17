def is_majority(arr: list, n: int, majority: int) -> bool:
  if arr.count(majority) > n//2:
    return True
  return False