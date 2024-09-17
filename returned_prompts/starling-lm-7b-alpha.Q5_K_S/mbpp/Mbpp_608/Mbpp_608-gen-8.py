
def bell_Number(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return sum([bell_Number(i) * bell_Number(n - 1 - i) for i in range(n)])


