import re
def find_literals(sentence: str, pattern: str) -> tuple:
  match = re.search(pattern, sentence)
  return (match.group(0), match.start(), match.end())