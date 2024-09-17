def get_total_number_of_sequences(m: int, n: int) -> int:
  if n == 1:
    return 1
  return sum([get_total_number_of_sequences(m, n-1) for i in range(1, m+1)])