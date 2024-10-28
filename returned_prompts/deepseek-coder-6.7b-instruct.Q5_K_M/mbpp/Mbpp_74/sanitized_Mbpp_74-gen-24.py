def is_samepatterns(lst, patterns):
  return all(x == y for x, y in zip(lst, patterns))