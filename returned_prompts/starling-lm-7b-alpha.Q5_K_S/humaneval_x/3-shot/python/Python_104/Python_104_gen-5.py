    def helper(n):
        digits = [int(d) for d in str(n)]
        return all(d % 2 == 1 for d in digits)

    return sorted(filter(helper, x))


