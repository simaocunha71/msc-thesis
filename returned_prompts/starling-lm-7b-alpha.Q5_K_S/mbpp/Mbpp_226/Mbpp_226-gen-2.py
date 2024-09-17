
def odd_values_string(s: str) -> str:
  return ''.join([i for i in s if (ord(i) % 2 != 0)])


