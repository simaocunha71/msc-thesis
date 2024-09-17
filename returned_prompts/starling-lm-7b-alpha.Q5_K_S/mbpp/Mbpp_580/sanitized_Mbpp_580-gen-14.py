def extract_even(mixed_tuple: tuple) -> tuple:
  even_tuple = tuple(filter(lambda x: len(x)%2 == 0, mixed_tuple))
  return even_tuple