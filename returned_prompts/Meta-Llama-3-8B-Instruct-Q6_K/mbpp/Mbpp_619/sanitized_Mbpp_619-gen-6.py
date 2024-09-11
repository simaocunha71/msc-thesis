def move_num(s: str) -> str:
  return ''.join(filter(str.isdigit, s)) + ''.join(filter(lambda x: not str.isdigit(x), s))  # or use re.sub