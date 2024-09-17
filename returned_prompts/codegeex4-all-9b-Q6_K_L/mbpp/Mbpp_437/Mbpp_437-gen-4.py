def remove_odd(s: str) -> str:
  new_s = ''
  for i in range(len(s)):
    if i % 2 == 0:
      new_s += s[i]
  return new_s

