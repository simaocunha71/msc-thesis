
def get_total_number_of_sequences(m: int, n: int):
  if n == 0:
    return 1
  return (m-1) + get_total_number_of_sequences(m-1, n-1)


