
def get_total_number_of_sequences(m: int, n: int) -> int:
  if n == 1:
    return m
  else:
    return get_total_number_of_sequences(m,n-1) * (m//2)


