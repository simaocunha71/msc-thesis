
def max_run_uppercase(s: str) -> int:
  run_count = 0
  max_run = 0
  for c in s:
    if c.isupper():
      run_count += 1
      if max_run < run_count:
        max_run = run_count
    else:
      run_count = 0
  return max_run


