
def replace_spaces(string: str) -> str:
  new_string = ""
  for c in string:
    if c == "_":
      new_string += " "
    else:
      new_string += c
  return new_string


