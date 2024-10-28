def centered_hexagonal_number(n: int) -> int:
  n_minus_1 = n - 1
  hexagonal_number = (n_minus_1 * (3 * n_minus_1 + 1)) // 2
  return hexagonal_number