
import re
def extract_values(string: str) -> list:
  pattern = re.compile(r'"(.+?)"')
  return re.findall(pattern, string)


