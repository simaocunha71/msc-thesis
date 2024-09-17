def catalan_number(n: int) -> int:
  if n == 0:
    return 1
  if n % 2 == 1:
    return (2*catalan_number(n-1)+catalan_number(n-2))//(n+1)
  return catalan_number(n-1)+catalan_number(n-2)