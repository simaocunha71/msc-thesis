
import re
def extract_quotation(str:str)->list:
  return re.findall(r'"(\w+)"',str)


