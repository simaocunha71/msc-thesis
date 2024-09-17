def max_run_uppercase(s: str) -> int:
  uppercase_count = 0
  current_run = 0
  for c in s:
    if c.isupper():
      current_run += 1
    else:
      if current_run > uppercase_count:
        uppercase_count = current_run
      current_run = 0
  if current_run > uppercase_count:
    uppercase_count = current_run
  return uppercase_count