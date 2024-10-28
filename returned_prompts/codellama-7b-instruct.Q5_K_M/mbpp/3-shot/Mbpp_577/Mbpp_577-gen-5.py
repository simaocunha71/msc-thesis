
def last_Digit_Factorial(n):
  if n<0:
    return -1
  if n==0:
    return 1
  result=1
  while(n>0):
    result*=n
    n-=1
  return result%10


