
import re
def extract_values(string_):
  return re.findall(r'"([^"]*)"', string_)


