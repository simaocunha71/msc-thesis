def division_elements(tuple_a: tuple, tuple_b: tuple) -> tuple:
  return tuple(a / b for a, b in zip(tuple_a, tuple_b))