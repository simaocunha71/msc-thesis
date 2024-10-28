def get_max_sum(n):
    memo = {}

    def find_max_sum(n):
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        memo[n] = max(n, find_max_sum(n // 2) + find_max_sum(n // 3) + find_max_sum(n // 4) + find_max_sum(n // 5))
        return memo[n]

    return find_max_sum(n)