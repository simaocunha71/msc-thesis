def is_perfect_square(n: int):
  if n < 0:
    return False
  if n == 0 or n == 1:
    return True
  root = int(n ** 0.5)
  return root * root == n