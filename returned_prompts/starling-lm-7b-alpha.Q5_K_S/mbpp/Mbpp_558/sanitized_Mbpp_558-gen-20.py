def digit_distance_nums(n: int,m: int) -> int:
  n_digits = [int(i) for i in str(n)]
  m_digits = [int(i) for i in str(m)]
  return sum([abs(i-j) for i,j in zip(n_digits,m_digits)])