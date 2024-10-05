    def helper(n, p):
        result = 1
        while n:
            if n % 2 == 1:
                result = result * result % p
            n = n // 2
            p = p ** 2 % 1009
        return result % p

    return helper(n, p)


