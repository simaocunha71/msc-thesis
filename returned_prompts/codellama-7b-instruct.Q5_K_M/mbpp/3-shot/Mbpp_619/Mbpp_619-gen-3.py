
import re
def move_num(s: str) -> str:
  s = re.sub('[0-9]+', '', s)
  return s


