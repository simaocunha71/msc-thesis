def substract_elements(tup1: tuple, tup2: tuple) -> tuple:
  return tuple([i-j for i, j in zip(tup1, tup2)])