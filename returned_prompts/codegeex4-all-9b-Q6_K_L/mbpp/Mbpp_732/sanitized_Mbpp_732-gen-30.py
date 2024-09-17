def replace_specialchar(text):
  special_chars = [' ', ',', '.']
  for char in special_chars:
    text = text.replace(char, ':')
  return text