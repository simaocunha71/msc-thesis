def odd_values_string(s):
  return "".join([i for i in s if not (index := str.index(s, i)) % 2 == 1])  # Python 3.8+