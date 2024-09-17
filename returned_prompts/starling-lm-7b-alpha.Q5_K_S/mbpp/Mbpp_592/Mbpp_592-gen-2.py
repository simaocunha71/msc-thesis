
def sum_Of_product(n: int) -> int:
  sum_ = 0
  for i in range(n+1):
    sum_ += ((i*(i+1))//2)
  return sum_


