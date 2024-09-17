
def even_binomial_Coeff_Sum(n):
  sum=0
  for i in range(0,n+1):
    if(i%2==0):
      sum+=binomialCoeff(n,i)
  return sum

def binomialCoeff(n,r):
  if(r==0 or r==n):
    return 1
  else:
    return binomialCoeff(n-1,r-1)+binomialCoeff(n-1,r)


