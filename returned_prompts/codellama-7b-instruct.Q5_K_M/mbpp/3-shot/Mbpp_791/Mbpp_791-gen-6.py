
def remove_nested(tuple_to_check):
  if isinstance(tuple_to_check, tuple):
    return tuple_to_check
  elif isinstance(tuple_to_check, list):
    return [remove_nested(num) for num in tuple_to_check]
  else:
    return tuple_to_check


