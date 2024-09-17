import re
def check_str(my_string: str) -> bool:
  if re.match(r'^[aeiouAEIOU]', my_string):
    return True
  else:
    return False