def snake_to_camel(snake_string: str) -> str:
  words = snake_string.split('_')
  camel_string = words[0]
  for word in words[1:]:
    camel_string += word[0].upper() + word[1:]
  return camel_string