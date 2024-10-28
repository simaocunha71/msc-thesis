
import re
def extract_quotation(s: str) -> list:
  pattern = re.compile(r'"(.*?)"')
  match = pattern.findall(s)
  return match


