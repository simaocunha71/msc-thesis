
def get_total_number_of_sequences(m: int, n: int) -> int:
  if n == 1:
    return 1
  if m // 2 < n:
    return 0
  return get_total_number_of_sequences(m, n-1) + get_total_number_of_sequences(m//2,n-1)


