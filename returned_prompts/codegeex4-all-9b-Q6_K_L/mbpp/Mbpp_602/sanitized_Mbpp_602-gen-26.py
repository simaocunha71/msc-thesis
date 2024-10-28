def first_repeated_char(string):
  char_freq = {}
  for char in string:
    if char in char_freq:
      return char
    char_freq[char] = 1
  return None