def divisor(n: int) -> int:
    divisor_count = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor_count += 1
    return divisor_count