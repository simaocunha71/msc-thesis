
def count_char_position(s: str) -> int:
  count = 0
  for i in range(26):
    c = chr(ord('a') + i)
    if s.lower().count(c) > 0:
      count += 1
  return count


