def newman_prime(n):
  p = 2
  while True:
    p = (p**2+1) % (2*n)
    if p<2:
      p+=1
    if p>n:
      return p-1