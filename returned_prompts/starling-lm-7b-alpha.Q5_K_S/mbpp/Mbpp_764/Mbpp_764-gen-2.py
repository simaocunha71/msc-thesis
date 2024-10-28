
def number_ctr(s: str) -> int:
  count = 0
  for i in s:
    if i.isdigit():
      count += 1
  return count


