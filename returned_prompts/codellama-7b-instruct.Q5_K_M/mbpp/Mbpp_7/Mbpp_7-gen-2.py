
def find_char_long(str):
  words = str.split()
  return [word for word in words if len(word) >= 4]


