def catalan_number(n: int) -> int:
  if n==0 or n==1:
    return 1
  else:
    return (2*(2*n-1)*catalan_number(n-1))//(n+1)

