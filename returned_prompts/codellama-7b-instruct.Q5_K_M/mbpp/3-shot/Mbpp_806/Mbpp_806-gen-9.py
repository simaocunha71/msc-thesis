
def max_run_uppercase(s: str) -> int:
  count = 0
  current_run = 0
  for i in range(len(s)):
    if s[i].isupper():
      current_run += 1
    else:
      current_run = 0
    count = max(count, current_run)
  return count


