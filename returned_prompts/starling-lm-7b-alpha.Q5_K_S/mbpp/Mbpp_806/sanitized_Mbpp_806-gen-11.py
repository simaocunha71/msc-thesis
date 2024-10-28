def max_run_uppercase(s: str) -> int:
  max_run = 0
  cur_run = 0
  for i in range(1, len(s)):
    if s[i].isupper() and s[i - 1].isupper():
      cur_run += 1
    else:
      cur_run = 0
    max_run = max(max_run, cur_run)
  return max_run + 1