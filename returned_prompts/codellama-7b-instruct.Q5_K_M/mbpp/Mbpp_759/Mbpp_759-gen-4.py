
def is_decimal(num_string):
  try:
    float(num_string)
    float(num_string).is_integer()
    return False
  except ValueError:
    return True


