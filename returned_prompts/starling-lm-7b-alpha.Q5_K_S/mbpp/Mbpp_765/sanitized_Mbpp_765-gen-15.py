def polite(num: int) -> int:
  if num < 2:
    return num
  else:
    return polite(len(str(num))) + int(str(num)[-1])
def is_polite(num: int) -> int:
  return polite(num)