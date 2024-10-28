
def find_remainder(lst, n):
  prod = 1
  for i in lst:
    prod = (prod * i) % n
  return prod


