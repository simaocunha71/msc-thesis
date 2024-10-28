def count_char_position(s: str) -> int:
  count = 0
  for i in range(len(s)):
    if ord(s[i].lower()) - ord('a') + 1 == i + 1:
      count += 1
  return count

