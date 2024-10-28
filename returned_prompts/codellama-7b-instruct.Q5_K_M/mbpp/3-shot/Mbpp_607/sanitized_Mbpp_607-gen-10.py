import re
def find_literals(str, pattern):
  m = re.search(pattern, str)
  if m:
    return m.group(), m.start(), m.end()
  else:
    return None, -1, -1