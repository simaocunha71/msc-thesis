from math import comb
def count_binary_seq(n):
  total = 0
  for i in range(2**n):
    first_n_bits = bin(i)[:n][2:]
    last_n_bits = bin(i)[n:][2:]
    if sum(int(bit) for bit in first_n_bits) == sum(int(bit) for bit in last_n_bits):
      total += 1
  return total / comb(2**n, n)