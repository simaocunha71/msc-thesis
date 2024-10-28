
def max_run_uppercase(s: str):
  max_run = 0
  current_run = 0
  for i in range(len(s)):
    if s[i].isupper():
      current_run += 1
    else:
      current_run = 0
    max_run = max(current_run, max_run)
  return max_run


