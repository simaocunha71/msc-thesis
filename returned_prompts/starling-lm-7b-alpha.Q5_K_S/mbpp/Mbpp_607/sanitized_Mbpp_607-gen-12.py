import re
def find_literals(string: str, pattern: str) -> tuple:
  match = re.search(pattern, string)
  return (match.group(), match.start(), match.end())