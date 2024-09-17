import re
def check_str(s):
  if re.match(r'^[aeiou]', s, re.I):
    return True
  return False