def tuple_str_int(s):
  return tuple(map(int, s.strip('()').split(',')))