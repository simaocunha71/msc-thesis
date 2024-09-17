
import re
def extract_values(s: str) -> list:
  pattern = r'"([^"]*)"'
  matches = re.findall(pattern, s)
  return matches


