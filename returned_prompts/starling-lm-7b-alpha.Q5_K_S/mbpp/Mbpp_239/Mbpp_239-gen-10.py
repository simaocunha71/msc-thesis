
def get_total_number_of_sequences(m: int, n: int) -> int:
  total_num = 0
  for i in range(1, m+1):
    total_num += min(m, i+i) - i
  return total_num


