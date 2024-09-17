
def even_binomial_Coeff_Sum(n):
  sum=0
  for i in range(0,n+1):
    if i%2==0:
      sum+=binomial_coefficient(n,i)
  return sum

def binomial_coefficient(n,k):
  if k==0 or k==n:
    return 1
  else:
    return binomial_coefficient(n-1,k-1)+binomial_coefficient(n-1,k)


