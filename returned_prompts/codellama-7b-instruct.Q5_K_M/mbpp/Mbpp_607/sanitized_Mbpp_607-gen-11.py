import re
def find_literals(text: str, pattern: str) -> tuple:
  match = re.search(pattern, text)
  if not match:
    return None, None, None
  else:
    return match.group(), match.start(), match.end()