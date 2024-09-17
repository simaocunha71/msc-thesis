import re
def move_num(input_str: str) -> str:
  return re.sub(r'[0-9]', '', input_str) + re.findall(r'\d+', input_str)