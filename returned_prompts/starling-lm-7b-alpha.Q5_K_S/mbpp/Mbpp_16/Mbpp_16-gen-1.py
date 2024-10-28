
def text_lowercase_underscore(input_str: str) -> bool:
  for char in input_str:
    if char == '_':
      for i in range(len(input_str)):
        if i == 0 and char == '_':
          pass
        elif char == '_' and i != 0:
          if ord(input_str[i-1]) >= 97 and ord(input_str[i+1]) >= 97:
            return True
  return False


