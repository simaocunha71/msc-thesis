
def max_run_uppercase(s):
  current = 0
  max_run = 0
  for c in s:
    if c.isupper():
      current += 1
      max_run = max(max_run, current)
    else:
      current = 0
  return max_run


