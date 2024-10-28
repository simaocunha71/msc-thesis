
def is_decimal(s):
  try:
    float(s)
  except ValueError:
    return False
  return s.count('.') == 1 and 0 <= len(s[s.index('.'):]) <= 3


