
def text_lowercase_underscore(text: str) -> bool:
  return re.fullmatch(r'^[a-z]+(_[a-z]+)*$', text)


