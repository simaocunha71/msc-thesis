def remove_uppercase(string_to_format: str) -> str:
  lowercase_string = ''
  for char in string_to_format:
    if char.islower():
      lowercase_string += char
  return lowercase_string