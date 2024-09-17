def count_char_position(s: str) -> int:
  count = 0
  for i in range(len(s)):
    if s[i].lower() == s[i]:
      count += 1
  return count