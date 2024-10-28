def max_run_uppercase(s: str) -> int:
  l = []
  for i in range(len(s)):
    if s[i].isupper():
      l.append(i)
  l.append(len(s))
  return l[1]-l[0]