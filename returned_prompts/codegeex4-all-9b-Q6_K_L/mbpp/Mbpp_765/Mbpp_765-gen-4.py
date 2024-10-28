def is_polite(n):
  def polite_numbers(n):
    yield 1
    yield 2
    for i in count(3):
      yield from range(i, 2*i, 2)
  return list(islice(polite_numbers(n), n))

