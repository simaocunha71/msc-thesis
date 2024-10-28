
import re
def extract_values(string_value: str) -> list:
  pattern = r'"(.*?)"'
  result = re.findall(pattern, string_value)
  return result


