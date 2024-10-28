    def helper(n):
        if n < 0:
            return False
        if n == 0:
            return True
        if n % 2 == 0:
            return False
        return helper(n // 10)

    return sorted([i for i in x if helper(i)])


