def first_repeated_char(s: str) -> str:
  count = {}
  for c in s:
    if c in count:
      return c
    count[c] = 1
  return None