
def next_power_of_2(n: int) -> int:
    if n == 0:
        return 1
    while n & (n-1):
        n = n & (n-1)
    return n << 1


