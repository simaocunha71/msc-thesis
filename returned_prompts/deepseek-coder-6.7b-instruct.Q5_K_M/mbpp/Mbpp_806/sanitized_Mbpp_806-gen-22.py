def max_run_uppercase(s):
  max_run = 0
  cur_run = 0
  for ch in s:
    if ch.isupper():
      cur_run += 1
    else:
      if cur_run > max_run:
        max_run = cur_run
      cur_run = 0
  return max(max_run, cur_run)