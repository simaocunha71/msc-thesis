from typing import List


def factorize(n: int) -> List[int]:
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        result.append(n)
    return result
