
def find_char_long(string):
  words = string.split(' ')
  return [word for word in words if len(word) >= 4]


