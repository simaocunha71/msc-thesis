
def replace_specialchar(text):
  special_char = ['.', ',', ' ']
  for char in special_char:
    text = text.replace(char, ':')
  return text


