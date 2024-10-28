def get_total_number_of_sequences(m, n):
  total_num = 0
  for i in range(n):
    total_num += m - i
  return total_num