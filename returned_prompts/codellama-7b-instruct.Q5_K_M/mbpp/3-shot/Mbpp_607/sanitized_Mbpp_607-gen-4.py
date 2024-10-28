import re
def find_literals(strng, pattern):
  match = re.search(pattern, strng)
  return match.group(0), match.start(), match.end()