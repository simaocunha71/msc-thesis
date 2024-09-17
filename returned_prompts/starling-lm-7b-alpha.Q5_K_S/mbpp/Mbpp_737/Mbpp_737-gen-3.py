
import re
def check_str(s: str) -> bool:
  vowels = "aeiou"
  if re.match("^[{}]".format(vowels), s):
    return True
  return False


