
import re
def move_num(num_str: str) -> str:
  pattern = re.compile(r'\d+')
  return pattern.sub('', num_str) + re.sub(pattern, '', num_str)


