
def nonagonal_num(n: int) -> int:
  if n == 0:
    return 0
  return (n*(6*n + 1))//7


