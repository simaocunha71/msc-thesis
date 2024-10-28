def get_max_sum(n):
    memo = {}
    def f(n):
        if n not in memo:
            max_sum = n
            if n % 2 == 0:
                max_sum = max(max_sum, f(n/2))
            if n % 3 == 0:
                max_sum = max(max_sum, f(n/3))
            if n % 4 == 0:
                max_sum = max(max_sum, f(n/4))
            if n % 5 == 0:
                max_sum = max(max_sum, f(n/5))

            memo[n] = max_sum
        return memo[n]
    return f(n)