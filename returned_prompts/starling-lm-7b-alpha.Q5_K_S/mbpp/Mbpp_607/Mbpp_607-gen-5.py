
import re
def find_literals(haystack:str, needle:str) -> tuple:
  match = re.search(needle, haystack)
  return match.group(), match.start(), match.end()


