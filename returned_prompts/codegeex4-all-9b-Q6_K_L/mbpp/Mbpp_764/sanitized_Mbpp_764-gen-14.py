def number_ctr(string: str) -> int:
  count = 0
  for char in string:
    if char.isdigit():
      count += 1
  return count