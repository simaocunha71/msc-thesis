
import re
def find_literals(s:str,p:str) -> tuple:
  return re.findall(p, s)


