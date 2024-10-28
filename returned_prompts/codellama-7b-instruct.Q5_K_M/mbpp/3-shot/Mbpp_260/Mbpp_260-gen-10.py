
def newman_prime(n):
  if n==1:
    return 2
  else:
    for i in range(3,n+1):
      if is_not_prime(i):
        continue
      else:
        return i


