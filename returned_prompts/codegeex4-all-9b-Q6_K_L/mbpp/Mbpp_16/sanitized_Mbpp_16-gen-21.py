def text_lowercase_underscore(text):
  pattern = r'^[a-z]+(_[a-z]+)*$'
  if re.match(pattern, text):
    return True
  return False