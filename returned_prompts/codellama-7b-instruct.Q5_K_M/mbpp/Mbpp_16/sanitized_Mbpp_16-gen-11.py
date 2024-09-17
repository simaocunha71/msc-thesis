import re
def text_lowercase_underscore(s: str) -> bool:
  return re.match(r"^[a-z]+(?:_[a-z]+)*$", s)