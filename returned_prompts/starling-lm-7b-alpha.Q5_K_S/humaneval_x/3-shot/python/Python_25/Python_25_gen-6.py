    def helper(n: int) -> None:
        if n == 1:
            return
        for i in range(2, n + 1):
            if i * i > n:
                break
            if n % i == 0:
                factors.append(i)
                helper(n // i)
                return

    factors = []
    helper(n)
    return factors


