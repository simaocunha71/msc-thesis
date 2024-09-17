def count_Pairs(lst: list, n: int) -> int:
  return sum(n-i-1 for i in range(n))