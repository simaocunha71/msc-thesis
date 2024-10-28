
def sumofFactors(num: int) -> int:
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    factors_even = [x for x in factors if x % 2 == 0]
    return sum(factors_even)


