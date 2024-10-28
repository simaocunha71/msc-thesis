def text_lowercase_underscore(text: str) -> bool:
  import re
  return bool(re.search(r'[a-z]+_[a-z]+', text))  # or return re.search(r'[a-z]+_[a-z]+', text) is not None