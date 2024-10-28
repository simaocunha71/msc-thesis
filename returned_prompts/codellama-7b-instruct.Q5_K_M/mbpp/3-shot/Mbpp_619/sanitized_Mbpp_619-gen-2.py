import re
def move_num(s):
  return re.sub(r'\d+', '', s) + re.sub(r'\d+', lambda m: str(int(m.group())), s)