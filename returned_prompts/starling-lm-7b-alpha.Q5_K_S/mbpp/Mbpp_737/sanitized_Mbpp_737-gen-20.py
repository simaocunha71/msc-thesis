import re
def check_str(s):
  if re.match(r'^[aeiouAEIOU]', s):
    return True
  else:
    return False