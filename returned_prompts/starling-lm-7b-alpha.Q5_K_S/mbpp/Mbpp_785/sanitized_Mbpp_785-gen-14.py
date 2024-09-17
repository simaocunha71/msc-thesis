def tuple_str_int(s:str)->tuple:
  return tuple(map(int, s[1:-1].split(',')))