import re
def check_str(input_str: str) -> bool:
  pattern = r"^[aeiouAEIOU]"
  if re.match(pattern, input_str):
    return True
  else:
    return False