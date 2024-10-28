def tuple_str_int(s):
  return tuple(map(int, s.strip('()').split(',')))  # strip off the parentheses, split on commas, convert to int, and then to a tuple