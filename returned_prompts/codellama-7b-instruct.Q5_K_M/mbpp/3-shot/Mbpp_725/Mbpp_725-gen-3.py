
import re
def extract_quotation(s: str) -> list:
  matches = re.findall(r'"(.*?)"', s)
  return matches


