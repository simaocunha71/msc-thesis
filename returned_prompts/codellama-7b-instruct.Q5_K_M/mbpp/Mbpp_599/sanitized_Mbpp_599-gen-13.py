def sum_average(n: int) -> tuple:
  sum_of_numbers = sum(range(1,n+1))
  average = sum_of_numbers/n
  return (sum_of_numbers, average)