
def extract_even(nested_tuple: tuple) -> tuple:
  return tuple(filter(lambda x: x % 2 == 0, nested_tuple))


