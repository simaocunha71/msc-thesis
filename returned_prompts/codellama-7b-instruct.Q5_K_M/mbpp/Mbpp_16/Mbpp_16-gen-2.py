
def text_lowercase_underscore(text: str) -> bool:
  if text.islower() and "_" in text:
    return True
  else:
    return False


