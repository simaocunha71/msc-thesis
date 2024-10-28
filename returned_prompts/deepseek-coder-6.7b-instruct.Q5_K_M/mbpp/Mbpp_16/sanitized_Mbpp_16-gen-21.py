import re
def text_lowercase_underscore(text):
  return bool(re.search(r'[a-z]+_[a-z]+', text))