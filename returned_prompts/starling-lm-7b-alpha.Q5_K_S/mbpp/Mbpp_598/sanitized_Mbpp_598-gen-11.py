def armstrong_number(n: int) -> bool:
  sum_of_digits = sum(map(int, str(n)))
  return sum_of_digits ** len(str(n)) == n