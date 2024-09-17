def sum_in_range(l: int, r: int) -> int:
  return sum(i for i in range(l, r+1) if i%2!=0)