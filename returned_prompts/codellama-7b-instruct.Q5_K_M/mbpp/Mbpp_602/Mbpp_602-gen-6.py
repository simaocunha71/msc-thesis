
def first_repeated_char(input_str):
  repeated_chars = []
  for char in input_str:
    if char in repeated_chars:
      return char
    else:
      repeated_chars.append(char)
  return None


