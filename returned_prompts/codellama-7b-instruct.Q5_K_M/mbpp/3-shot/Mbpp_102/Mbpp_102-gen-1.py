
def snake_to_camel(snake_case_str: str) -> str:
  camel_case_str = ""
  for word in snake_case_str.split('_'):
    camel_case_str += word[0].upper() + word[1:]
  return camel_case_str


