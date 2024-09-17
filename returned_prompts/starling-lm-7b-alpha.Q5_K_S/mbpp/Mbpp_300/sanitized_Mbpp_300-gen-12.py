from math import factorial
def count_binary_seq(n: int) -> float:
  return factorial(2*n) // (factorial(n) ** 2)