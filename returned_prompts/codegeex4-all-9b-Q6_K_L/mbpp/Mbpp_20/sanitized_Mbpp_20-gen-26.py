import math
def is_woodall(n: int) -> bool:
    if n < 2:
        return False
    sum = 0
    for i in range(1, n + 1):
        sum += math.factorial(i)
    return sum == n