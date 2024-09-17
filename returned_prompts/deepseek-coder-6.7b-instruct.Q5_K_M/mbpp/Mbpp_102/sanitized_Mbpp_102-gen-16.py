def snake_to_camel(s):
  return ''.join(i.capitalize() for i in s.split('_'))