
import re
def find_literals(string: str, pattern: str) -> tuple:
  index = re.search(pattern, string)
  return (index.group(), index.start(), index.end())


