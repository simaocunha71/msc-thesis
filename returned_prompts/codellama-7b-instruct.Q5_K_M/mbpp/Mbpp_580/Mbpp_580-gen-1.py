
def extract_even(nested_tuple):
  return tuple(filter(lambda x: not isinstance(x, tuple) or x%2==0,nested_tuple))


