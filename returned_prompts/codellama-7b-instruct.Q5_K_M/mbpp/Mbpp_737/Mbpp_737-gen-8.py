
import re
def check_str(str1: str) -> bool:
  pattern = re.compile(r"^[aeiouAEIOU]")
  if pattern.match(str1):
    return True
  else:
    return False


