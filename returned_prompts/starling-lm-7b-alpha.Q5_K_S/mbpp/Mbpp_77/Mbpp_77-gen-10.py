
def is_Diff(n: int) -> bool:
  return abs(sum(map(int, str(n))) - (n % 11)) < 2


