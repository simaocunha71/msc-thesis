def snake_to_camel(snake_string: str) -> str:
  return ''.join(word.title() for word in snake_string.split('_'))