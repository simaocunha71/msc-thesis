def remove_odd(string: str) -> str:
  new_string = ""
  for char in string:
    if char % 2 == 0:
      new_string += char
  return new_string