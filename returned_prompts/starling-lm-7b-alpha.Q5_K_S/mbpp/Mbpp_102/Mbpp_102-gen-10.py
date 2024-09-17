
def snake_to_camel(snake_case_string: str) -> str:
  camel_case_string = snake_case_string[0].upper() + snake_case_string[1:]
  for i in range(len(snake_case_string)):
    if snake_case_string[i] == '_':
      camel_case_string += snake_case_string[i+1].upper()
  return camel_case_string


