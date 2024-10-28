
import re
def check_str(str):
  if re.match('^[aeiouAEIOU]', str):
    return True
  return False


