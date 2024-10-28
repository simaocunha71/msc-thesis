
def get_total_number_of_sequences(m: int,n: int) -> int:
  total_sequences = 0
  for i in range(1,n+1):
    total_sequences += m//i
  return total_sequences


