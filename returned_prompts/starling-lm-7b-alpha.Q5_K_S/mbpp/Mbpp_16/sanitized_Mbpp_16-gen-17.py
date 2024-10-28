def text_lowercase_underscore(text:str) -> bool:
  for i in range(len(text)-1):
    if text[i].islower() and "_" in text[i+1]:
      return True
  return False