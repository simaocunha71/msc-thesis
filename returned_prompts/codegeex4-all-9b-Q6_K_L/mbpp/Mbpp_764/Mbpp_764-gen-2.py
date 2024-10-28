def number_ctr(s: str) -> int:
  return sum(c.isdigit() for c in s)

