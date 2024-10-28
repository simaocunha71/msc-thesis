import re
def check_str(input_str: str) -> bool:
  pattern = re.compile(r'^[aeiou]')
  if pattern.match(input_str):
    return True
  else:
    return False