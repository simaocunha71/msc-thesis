def count_binary_seq(n):
  return binomial_coefficient(2*n, n)
def binomial_coefficient(n, k):
  if k < 0 or n < k:
    return 0
  if k == 0 or n == k:
    return 1
  return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)