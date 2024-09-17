def remove_uppercase(s: str) -> str:
  new_s = ''
  for c in s:
    if c.islower():
      new_s += c
  return new_s

