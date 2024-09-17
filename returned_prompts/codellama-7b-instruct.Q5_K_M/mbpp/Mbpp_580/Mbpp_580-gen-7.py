
def extract_even(nested_tuple: tuple) -> tuple:
  result = ()
  for element in nested_tuple:
    if isinstance(element, tuple):
      element = extract_even(element)
      if element:
        result += (element,)
    elif element % 2 == 0:
      result += (element,)
  return result


