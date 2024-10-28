
def extract_even(tup):
  result = ()
  for elem in tup:
    if isinstance(elem, tuple):
      result += (extract_even(elem),)
    else:
      if elem % 2 == 0:
        result += (elem,)
  return result


