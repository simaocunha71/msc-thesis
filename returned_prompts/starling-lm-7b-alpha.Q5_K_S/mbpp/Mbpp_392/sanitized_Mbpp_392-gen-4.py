def get_max_sum(n):
    """
    :type n: int
    :rtype: int
    """
    def f(n):
        if n in memo: return memo[n]
        if n < 1: return 0
        res = max((f(n/2) + f(n/3) + f(n/4) + f(n/5)), n)
        memo[n] = res
        return res
    memo = {}
    return f(n)