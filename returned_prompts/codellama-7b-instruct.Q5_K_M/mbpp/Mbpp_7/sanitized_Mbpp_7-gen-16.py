def find_char_long(text):
  words = text.split()
  return [word for word in words if len(word) >= 4]