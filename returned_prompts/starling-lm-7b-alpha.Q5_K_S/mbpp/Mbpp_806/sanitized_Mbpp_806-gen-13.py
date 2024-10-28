def max_run_uppercase(s: str) -> int:
  count = 0
  max_count = 0
  for i in range(len(s)):
    if s[i].isupper():
      count += 1
      if count > max_count:
        max_count = count
    else:
      count = 0
  return max_count