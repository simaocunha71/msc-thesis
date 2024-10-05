

def largest_divisor(n: int) -> int:
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0:
            return i
    return 1

# 100%
