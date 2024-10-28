def is_majority(arr: list,n: int, elem: int) -> bool:
  count = 0
  for i in arr:
    if i == elem:
      count += 1
  if count > n//2:
    return True
  else:
    return False