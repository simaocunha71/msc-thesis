def is_undulating(num: int) -> bool:
  num = str(num)
  pattern = [num[0], num[1], num[0], num[1]]
  return pattern == num