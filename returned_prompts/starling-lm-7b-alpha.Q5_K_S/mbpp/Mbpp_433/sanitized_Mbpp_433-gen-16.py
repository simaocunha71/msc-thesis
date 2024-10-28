def check_greater(arr: list, target: int) -> bool:
  for i in arr:
    if i > target:
      return True
  return False