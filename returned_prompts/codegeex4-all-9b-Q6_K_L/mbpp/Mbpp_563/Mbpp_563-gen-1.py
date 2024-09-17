import re
def extract_values(string: str) -> list:
  pattern = r'"([^"]*)"'
  return re.findall(pattern, string)


