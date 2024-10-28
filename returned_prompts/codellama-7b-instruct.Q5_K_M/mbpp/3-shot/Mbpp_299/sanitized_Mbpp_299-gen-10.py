def max_aggregate(scores: list) -> tuple:
  name, aggregate = 0, 0
  for (n, a) in scores:
    if a > aggregate:
      name, aggregate = n, a
    else:
      aggregate += a
  return name, aggregate