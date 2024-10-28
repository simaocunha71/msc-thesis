def count_char_position(s: str) -> int:
  count = 0
  for char in s:
    if char.lower() == char and char.isalpha():
      count += 1
  return count