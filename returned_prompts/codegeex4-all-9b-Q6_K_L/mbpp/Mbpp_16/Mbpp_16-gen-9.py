def text_lowercase_underscore(text: str) -> bool:
  for i in range(len(text)-1):
    if text[i] == '_':
      if not text[i+1].islower():
        return False
  return True

