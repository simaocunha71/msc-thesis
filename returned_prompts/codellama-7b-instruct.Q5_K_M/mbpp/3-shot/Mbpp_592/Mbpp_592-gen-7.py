
def sum_Of_product(n):
  sum_of_product = 0
  for i in range(1,n+1):
    sum_of_product += binomial_coefficient(i, 2)
  return sum_of_product

def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


