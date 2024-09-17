def count_char_position(s: str):
  count = 0
  for i in range(len(s)):
    if ord(s[i]) - ord('a') == i:
      count += 1
  return count