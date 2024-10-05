    def helper(n, cur=0):
        if n == 0:
            return []
        if n % 2 == 0:
            return [cur + 2] + helper(n - 1, cur + 2)
        else:
            return [cur + 1] + helper(n - 1, cur + 1)

    return helper(n)


