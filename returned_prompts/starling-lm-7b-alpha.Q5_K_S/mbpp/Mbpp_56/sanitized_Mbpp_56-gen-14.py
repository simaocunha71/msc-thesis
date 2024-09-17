def check(n):
  n_str = str(n)
  if len(n_str) % 2 != 0:
    return False
  mid = len(n_str) // 2
  left = int(n_str[:mid])
  right = int(n_str[::-1][:mid])
  return left * 2 - 1 == right