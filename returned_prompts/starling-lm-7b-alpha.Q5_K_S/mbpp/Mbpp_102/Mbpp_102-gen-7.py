
def snake_to_camel(snake_string:str) -> str:
  return ''.join(x for x in snake_string.title() if not x.isupper())


