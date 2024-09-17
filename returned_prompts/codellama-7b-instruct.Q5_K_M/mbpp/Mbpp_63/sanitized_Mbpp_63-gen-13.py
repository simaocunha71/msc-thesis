def max_difference(pairs: list) -> int:
  return max([abs(a-b) for a, b in pairs])