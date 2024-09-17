import math
def count_binary_seq(n: int) -> float:
  return 2**n * math.factorial(n) / math.factorial(n+n)