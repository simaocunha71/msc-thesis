def check_integer(string_to_test):
  try:
    int(string_to_test)
    return True
  except ValueError:
    return False