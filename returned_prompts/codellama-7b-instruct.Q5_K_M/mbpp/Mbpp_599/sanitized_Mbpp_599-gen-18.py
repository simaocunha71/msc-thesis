def sum_average(n: int) -> tuple:
  sum_of_n_numbers = (n * (n + 1)) // 2
  average_of_n_numbers = sum_of_n_numbers / n
  return sum_of_n_numbers, average_of_n_numbers