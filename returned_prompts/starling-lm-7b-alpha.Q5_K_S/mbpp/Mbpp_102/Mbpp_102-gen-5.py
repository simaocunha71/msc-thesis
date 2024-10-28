
def snake_to_camel(snake_case_string: str) -> str:
  return ''.join(word.title() for word in snake_case_string.split('_'))


