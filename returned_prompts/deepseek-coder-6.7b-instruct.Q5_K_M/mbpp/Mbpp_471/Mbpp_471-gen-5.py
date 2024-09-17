
def find_remainder(lst: list,n: int) -> int:
  prod = 1
  for num in lst:
    prod = (prod * num) % n
  return prod


