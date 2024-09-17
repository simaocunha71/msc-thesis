def toggle_string(s: str) -> str:
  new_string = ""
  for char in s:
    if char.islower():
      new_string += char.upper()
    elif char.isupper():
      new_string += char.lower()
    else:
      new_string += char
  return new_string