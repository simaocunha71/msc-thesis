
import re
def extract_values(str_val: str) -> list:
  pattern = re.compile('"[^"]+"')
  return [i.strip('"') for i in re.findall(pattern, str_val)]


