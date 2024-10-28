import re
def find_literals(string: str, pattern: str) -> tuple:
  match = re.search(pattern, string)
  return (match.group(0), match.start(), match.end())