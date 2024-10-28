
def snake_to_camel(snake_case_string):
  parts = snake_case_string.split('_')
  return parts[0] + ''.join(part.title() for part in parts[1:])


