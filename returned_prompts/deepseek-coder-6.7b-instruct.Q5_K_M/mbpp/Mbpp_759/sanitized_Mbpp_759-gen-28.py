def is_decimal(s):
  try:
    float(s)
  except ValueError:
    return False
  else:
    return s.count('.') == 1 and len(s.split('.')[1]) == 2