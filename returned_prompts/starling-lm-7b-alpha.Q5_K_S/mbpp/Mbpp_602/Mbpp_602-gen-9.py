
def first_repeated_char(s: str) -> str:
  char_count = {}
  for char in s:
    if char in char_count.keys():
      return char
    char_count[char] = 1
  return None


