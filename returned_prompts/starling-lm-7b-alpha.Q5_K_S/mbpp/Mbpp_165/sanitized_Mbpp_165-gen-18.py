def count_char_position(s: str) -> int:
  count = 0
  for i, letter in enumerate(s):
    if ord(letter.lower()) - i == 0:
      count += 1
  return count