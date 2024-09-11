from math import comb
def count_binary_seq(n):
  total = 0
  for i in range(2**n):
    first_n_sum = bin(i)[:n].count('1')
    last_n_sum = n - first_n_sum
    if first_n_sum == last_n_sum:
      total += 1
  return total + comb(2**n, n) * comb(2**n, n) / (2**n)  # add the number of sequences where the first and last n bits are all 0 or all 1