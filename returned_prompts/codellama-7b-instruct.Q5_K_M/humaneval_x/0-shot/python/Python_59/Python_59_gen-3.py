
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 1. 找到最小的质数，它一定是n的因子，因为n > 1 且n不是质数
    # 2. 检查该质数是否是n的最大质因数
    # 3. 如果是，返回该质数
    # 4. 否则，将该质数除掉，并从步骤1开始
    if n < 2:
        return None
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return None


# 1. 找到最小的质数，它一定是n的因子，因为n > 1 且n不是质数
# 2. 检查该质数是否是n的最大质因数
# 3. 如果是，返回该质数
# 4. 否则，将该质数除掉，并从步骤1开始
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return None
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) +