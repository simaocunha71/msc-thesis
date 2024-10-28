
import re
def check_str(s: str) -> bool:
  return bool(re.match(r'^[aeiou]', s, re.IGNORECASE))


