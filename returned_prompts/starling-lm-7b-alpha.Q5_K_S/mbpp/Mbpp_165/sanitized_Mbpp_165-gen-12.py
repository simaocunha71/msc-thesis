def count_char_position(s: str) -> int:
  count = 0
  for i, c in enumerate(s):
    if ord(c) - i == 97:
      count += 1
  return count