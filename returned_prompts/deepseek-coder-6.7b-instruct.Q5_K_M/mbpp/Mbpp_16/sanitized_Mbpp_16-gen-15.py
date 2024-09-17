def text_lowercase_underscore(text: str) -> bool:
  return all(x.islower() or x=='_' for x in text.split('_'))