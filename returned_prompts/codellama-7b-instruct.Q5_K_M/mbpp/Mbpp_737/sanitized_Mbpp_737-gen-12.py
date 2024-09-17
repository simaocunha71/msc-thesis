import re
def check_str(str):
  if re.match(r"^[aeiouAEIOU]",str):
    return True
  else:
    return False