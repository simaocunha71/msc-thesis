def count_char_position(s):
  count = 0
  for i, c in enumerate(s):
    if c.lower() == chr(97 + i):
      count += 1
  return count