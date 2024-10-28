def snake_to_camel(s: str) -> str:
  return ''.join(word.title() for word in s.split('_'))