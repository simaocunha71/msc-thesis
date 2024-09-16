"""
def get_max_sum(n):
    memo = {1: 1}
    def dfs(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return n
        memo[n] = max(dfs(n//2) + dfs(n//3) + dfs(n//4) + dfs(n//5), n)
        return memo[n]
    return dfs(n)
"""
