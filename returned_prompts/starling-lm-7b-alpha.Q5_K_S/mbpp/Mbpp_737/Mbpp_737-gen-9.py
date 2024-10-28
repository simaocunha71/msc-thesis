
import re
def check_str(s:str):
  return bool(re.match("^[AEIOUaeiou]", s))


