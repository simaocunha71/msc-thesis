def is_decimal(num_str):
  try:
    float(num_str)
    if len(num_str.split('.')[-1]) == 2:
      return True
    else:
      return False
  except ValueError:
    return False

