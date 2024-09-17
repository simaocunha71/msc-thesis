
def odd_values_string(s: str):
  return ''.join(c for i,c in enumerate(s) if i % 2 != 0)


