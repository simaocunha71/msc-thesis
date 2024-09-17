
def sum_Of_product(n):
  sum=0
  for i in range(0,n):
    sum+=((binomial_co_efficient(n,i))*(binomial_co_efficient(n,i+1)))
  return sum

def binomial_co_efficient(n,k):
  return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


