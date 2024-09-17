
import re
def extract_quotation(string):
  pattern = re.compile(r'\"(.*?)\"')
  return pattern.findall(string)


