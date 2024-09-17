def get_max_sum(n):
    memo = {1: 1}
    def recurse(n):
        if n in memo:
            return memo[n]
        memo[n] = max(n, recurse(n//2) + recurse(n//3) + recurse(n//4) + recurse(n//5))
        return memo[n]
    return recurse(n)