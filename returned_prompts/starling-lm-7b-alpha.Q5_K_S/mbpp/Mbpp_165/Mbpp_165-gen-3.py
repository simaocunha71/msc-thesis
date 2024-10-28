
def count_char_position(s: str) -> int:
  count = 0
  for i, c in enumerate(s):
    if ord(c.lower()) - i == 0:
      count += 1
  return count


