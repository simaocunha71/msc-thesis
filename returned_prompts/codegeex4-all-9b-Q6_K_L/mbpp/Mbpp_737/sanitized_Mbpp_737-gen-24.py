import re
def check_str(s: str):
  pattern = r'^[aeiou]'
  if re.search(pattern, s):
    return True
  else:
    return False