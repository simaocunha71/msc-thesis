def snake_to_camel(s):
  s = s.split('_')
  return ''.join(word.capitalize() for word in s) if len(s) > 1 else s[0].capitalize() if s else ''