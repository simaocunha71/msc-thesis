from math import comb
def count_binary_seq(n):
  total = 2**n
  return int(comb(total, n)) * 2