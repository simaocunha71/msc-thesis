def text_lowercase_underscore(text: str) -> bool:
  return all(char.islower() for char in text) and "_" in text


