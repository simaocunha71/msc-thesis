def extract_even(nested_tuple):
  result = ()
  for element in nested_tuple:
    if isinstance(element, tuple):
      result += extract_even(element)
    elif element % 2 == 0:
      result += (element,)
  return result