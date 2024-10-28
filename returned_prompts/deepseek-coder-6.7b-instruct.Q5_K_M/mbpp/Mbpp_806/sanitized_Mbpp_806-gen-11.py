def max_run_uppercase(s: str) -> int:
  max_count = 0
  count = 0
  for ch in s:
    if ch.isupper():
      count += 1
      if count > max_count:
        max_count = count
    else:
      count = 0
  return max_count