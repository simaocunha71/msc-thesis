import re
def find_literals(s: str, p: str) -> tuple:
  match = re.search(p, s)
  return (match.group(), match.start(), match.end())