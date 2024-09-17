
import math
def count_binary_seq(n: int) -> int:
    return math.factorial(2*n) / (math.factorial(n) ** 2)


