
import re
def extract_quotation(s: str):
  return re.findall(r'"([^"]*)"', s)


