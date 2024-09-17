
def is_samepatterns(patterns: list, values: list) -> bool:
  return len(set(zip(patterns, values))) == len(patterns)


