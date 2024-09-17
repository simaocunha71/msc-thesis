
def get_total_number_of_sequences(m: int, n: int) -> int:
  total_nums = 0
  for i in range(1, m+1):
    total_nums += min(i+1, m//i)
  return total_nums


