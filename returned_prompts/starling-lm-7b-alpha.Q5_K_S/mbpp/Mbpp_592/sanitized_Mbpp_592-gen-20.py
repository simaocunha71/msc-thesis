def sum_Of_product(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  return sum_Of_product(n-1) + sum_Of_product(n-2) + n