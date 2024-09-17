import re
def extract_quotation(string: str) -> list:
  pattern = r'"(.*?)"'
  extracted_elements = re.findall(pattern, string)
  return extracted_elements