import re
def check_str(given_str):
  if re.match("^[aeiou]", given_str):
    return True
  else:
    return False