def count_char_position(s: str) -> int:
  count = 0
  for i in range(len(s)):
    if ord(s[i].lower()) - i == 0:
      count += 1
  return count