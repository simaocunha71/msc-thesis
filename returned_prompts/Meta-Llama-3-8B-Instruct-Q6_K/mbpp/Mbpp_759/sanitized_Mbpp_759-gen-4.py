def is_decimal(s):
  if not isinstance(s, str):
    return False
  if not s.lstrip('-').replace('.','',1).replace('-','',1).isdigit():
    return False
  return len(s.split('.')[1]) <= 2