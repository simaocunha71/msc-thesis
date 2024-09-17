def count_char_position(s: str) -> int:
  count = 0
  for i, char in enumerate(s.lower()):
    if char == "a" + i:
      count += 1
  return count