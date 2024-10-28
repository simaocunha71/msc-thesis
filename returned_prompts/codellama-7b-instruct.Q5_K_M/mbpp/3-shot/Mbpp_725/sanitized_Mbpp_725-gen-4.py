import re
def extract_quotation(my_str: str) -> list:
  pattern = re.compile('"([^"]*)"')
  return [match.group(1) for match in pattern.finditer(my_str)]