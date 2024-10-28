
from math import comb
def sum_Of_product(n):
  return sum(comb(n, i)*comb(n, i+1) for i in range(n-1))


