def even_binomial_Coeff_Sum(n: int):
  return sum([binomialCoeff(n, 2*i) for i in range(n+1) if i % 2 == 0])
def binomialCoeff(n: int, k: int):
  C = [0]*(k+1)
  C[0] = 1
  for i in range(1, n + 1):
    for j in range(min(i, k), 0, -1):
      C[j] = C[j] + C[j-1]
  return C[k]