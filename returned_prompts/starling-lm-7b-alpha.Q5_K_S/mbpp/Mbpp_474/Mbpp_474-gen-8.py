
def replace_char(string: str, char1: str, char2: str) -> str:
  new_str = ""
  for i in range(len(string)):
    if string[i] == char1:
      new_str += char2
    else:
      new_str += string[i]
  return new_str


