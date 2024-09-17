
def sumofFactors(n):
  factors = [i for i in range(1,n+1) if n%i==0]
  return sum([i for i in factors if i%2==0])


