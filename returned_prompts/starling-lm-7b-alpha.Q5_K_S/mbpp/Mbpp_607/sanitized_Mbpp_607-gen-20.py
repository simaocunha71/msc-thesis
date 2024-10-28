import re
def find_literals(str_search: str, pattern: str) -> tuple:
  match = re.search(pattern, str_search)
  if match:
    return (match.group(), match.start(), match.end())
  else:
    return None