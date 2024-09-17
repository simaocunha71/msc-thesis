import re
def find_literals(string: str, pattern: str) -> tuple:
  matches = re.findall(pattern, string)
  if not matches:
    return None
  else:
    return matches[0]