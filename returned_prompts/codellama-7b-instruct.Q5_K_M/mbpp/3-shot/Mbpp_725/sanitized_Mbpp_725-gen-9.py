import re
def extract_quotation(s: str) -> list:
  return re.findall(r'"\w+"', s)