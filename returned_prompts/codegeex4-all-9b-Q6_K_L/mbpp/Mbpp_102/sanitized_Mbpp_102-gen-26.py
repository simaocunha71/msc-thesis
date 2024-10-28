def snake_to_camel(s: str) -> str:
  camel_s = ''.join(word.capitalize() for word in s.split('_'))
  return camel_s