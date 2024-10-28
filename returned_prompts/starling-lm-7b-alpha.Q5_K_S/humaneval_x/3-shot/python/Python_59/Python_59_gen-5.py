    def helper(n, i):
        if i * i > n:
            return n
        while n % i == 0:
            n //= i
        return helper(n, i + 1)
    return helper(n, 2)


