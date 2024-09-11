def even_binomial_Coeff_Sum(n):
  total = 0
  for k in range(n):
    if k % 2 == 0:
      total += binomial_coefficient(n, k)
  return total
def binomial_coefficient(n, k):
  if k > n - k: # take advantage of the symmetry
    k = n - k
  result = 1
  for i in range(1, k + 1):
    result = result * (n - i + 1) // i
  return result