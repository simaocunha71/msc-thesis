
def extract_even(tpl: tuple) -> tuple:
  return tuple(filter(lambda x: isinstance(x, int) and x % 2 == 0, tpl))


