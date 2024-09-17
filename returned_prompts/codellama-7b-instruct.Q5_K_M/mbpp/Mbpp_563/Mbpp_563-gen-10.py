
import re
def extract_values(string_input):
  values = re.findall(r'"([^"]*)"', string_input)
  return values


