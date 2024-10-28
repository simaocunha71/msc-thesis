def is_octagonal(n: int) -> int:
  octagonal_num = (3*n*(n-1) + 1) // 2
  return octagonal_num