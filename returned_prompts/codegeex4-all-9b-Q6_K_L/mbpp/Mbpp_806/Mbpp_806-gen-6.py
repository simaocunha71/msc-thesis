def max_run_uppercase(string):
  max_len = 0
  current_len = 0
  for char in string:
    if char.isupper():
      current_len += 1
      max_len = max(max_len, current_len)
    else:
      current_len = 0
  return max_len
