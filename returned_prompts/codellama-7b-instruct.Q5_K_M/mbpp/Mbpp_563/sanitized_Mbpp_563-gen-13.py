import re
def extract_values(string: str) -> list:
  matches = re.findall(r'"([^"]*)"', string)
  return matches