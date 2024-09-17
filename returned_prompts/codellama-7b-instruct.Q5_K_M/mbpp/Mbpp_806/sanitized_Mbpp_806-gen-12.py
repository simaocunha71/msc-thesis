def max_run_uppercase(s: str) -> int:
  current_run = 0
  max_run = 0
  for c in s:
    if c.isupper():
      current_run += 1
    else:
      if current_run > max_run:
        max_run = current_run
      current_run = 0
  if current_run > max_run:
    max_run = current_run
  return max_run