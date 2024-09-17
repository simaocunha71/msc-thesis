import re
def extract_quotation(string_text: str) -> list:
  return re.findall(r'"([^"]*)"', string_text)