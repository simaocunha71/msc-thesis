def max_run_uppercase(s: str) -> int:
  l = len(s)
  count = 0
  current = 0
  for i in range(l):
    if s[i].isupper():
      current += 1
    else:
      count = max(count, current)
      current = 0
  return max(count, current)