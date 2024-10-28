import re
def find_literals(s: str, pattern: str) -> tuple:
  match = re.search(pattern, s)
  return match.group(), match.start(), match.end()