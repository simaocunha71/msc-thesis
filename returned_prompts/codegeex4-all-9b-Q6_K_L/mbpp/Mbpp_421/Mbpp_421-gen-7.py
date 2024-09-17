def concatenate_tuple(tup: tuple, delimiter: str = "-") -> str:
  return delimiter.join(str(i) for i in tup)

