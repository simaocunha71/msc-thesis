
def count_char_position(s: str) -> int:
  count = 0
  for c in s:
    if c.lower() == chr(ord('a') + s.lower().index(c.lower())):
      count += 1
  return count


