def get_max_sum(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Memoization
    memo = {}
    def max_sum(n):
        if n in memo:
            return memo[n]
        if n == 0:
            memo[n] = 0
            return 0
        if n == 1:
            memo[n] = 1
            return 1

        # Recursive case
        memo[n] = max(n, max_sum(n//2) + max_sum(n//3) + max_sum(n//4) + max_sum(n//5))
        return memo[n]

    return max_sum(n)