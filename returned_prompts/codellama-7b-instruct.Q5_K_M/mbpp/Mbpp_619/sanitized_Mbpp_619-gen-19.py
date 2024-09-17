import re
def move_num(s: str) -> str:
  return re.sub(r'\d+', '', s) + re.sub(r'\d+', lambda x: str(x.group()), s)