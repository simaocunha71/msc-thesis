def max_run_uppercase(s: str) -> int:
  count = 0
  max_count = 0
  for c in s:
    if c.isupper():
      count += 1
    else:
      count = 0
    max_count = max(max_count, count)
  return max_count