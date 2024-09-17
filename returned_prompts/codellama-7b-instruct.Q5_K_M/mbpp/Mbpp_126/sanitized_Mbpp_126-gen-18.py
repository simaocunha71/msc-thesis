def sum(a,b):
  divisors = [d for d in range(1, min(a,b)+1) if a%d==0 and b%d==0]
  return sum(divisors)