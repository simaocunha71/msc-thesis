def is_undulating(n):
  n_str = str(n)
  if n_str[0] == n_str[-1]:
    return False
  for i in range(1, len(n_str)-1):
    if n_str[i] == n_str[i-1] or n_str[i] == n_str[i+1]:
      return False
  return True