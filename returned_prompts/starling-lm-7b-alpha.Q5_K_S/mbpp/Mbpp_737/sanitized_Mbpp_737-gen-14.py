import re
def check_str(string: str) -> bool:
  if re.match(r"^[aeiouAEIOU].*", string):
    return True
  else:
    return False