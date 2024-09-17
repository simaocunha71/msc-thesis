def extract_even(mixed_tup):
  def extract_even_helper(tup):
    if isinstance(tup, tuple):
      return tuple(extract_even_helper(i) for i in tup if isinstance(i, int) and i % 2 == 0 or extract_even_helper(i))
    else:
      return tup

  return extract_even_helper(mixed_tup)

