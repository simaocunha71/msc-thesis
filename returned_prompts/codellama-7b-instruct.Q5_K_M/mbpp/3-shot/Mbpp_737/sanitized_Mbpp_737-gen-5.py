import re
def check_str(word:str) -> bool:
  pattern = re.compile(r'^[aeiou]', re.IGNORECASE)
  if pattern.match(word):
    return True
  else:
    return False