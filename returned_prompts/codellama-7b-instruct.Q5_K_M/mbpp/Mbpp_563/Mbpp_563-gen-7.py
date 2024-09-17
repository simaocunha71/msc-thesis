
import re
def extract_values(string_input: str) -> list:
  result = re.findall(r'"(.*?)"', string_input)
  return result


