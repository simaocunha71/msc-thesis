def snake_to_camel(snake_str: str) -> str:
  components = snake_str.split('_')
  return ''.join(x.title() for x in components)


