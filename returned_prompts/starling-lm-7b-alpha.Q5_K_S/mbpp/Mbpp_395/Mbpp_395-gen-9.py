
def first_non_repeating_character(s: str) -> str:
  char_count = {}
  for ch in s:
    if ch in char_count:
      char_count[ch] += 1
    else:
      char_count[ch] = 1
  for ch in s:
    if char_count[ch] == 1:
      return ch
  return None


