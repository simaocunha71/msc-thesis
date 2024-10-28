def max_run_uppercase(s: str) -> int:
  start = 0
  max_run = 0
  for i in range(len(s)):
    if not s[i].isupper():
      start = i + 1
    if i - start + 1 > max_run:
      max_run = i - start + 1
  return max_run