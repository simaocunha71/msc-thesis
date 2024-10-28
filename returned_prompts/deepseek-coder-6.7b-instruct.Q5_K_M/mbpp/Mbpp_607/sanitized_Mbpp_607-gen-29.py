import re
def find_literals(text, pattern):
  match = re.search(pattern, text)
  return (match.group(), match.start(), match.end())