
def binomial_Coeff(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]

    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1

            # Calculate value using previously stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]

def even_binomial_Coeff_Sum(n: int) -> int:
  sum = 0
  for k in range(n+1):
    if k % 2 == 0:
      sum += binomial_Coeff(n,k)
  return sum


