
import re
def find_literals(string, pattern):
  found = re.search(pattern, string)
  if found:
    return found.group(), found.start(), found.end()
  else:
    return None, None, None


