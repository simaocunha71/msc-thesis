def count_char_position(s: str) -> int:
  count = 0
  for i, c in enumerate(s):
    for j, d in enumerate(s):
      if c.lower() == d.lower() and i == j:
        count += 1
        break
  return count