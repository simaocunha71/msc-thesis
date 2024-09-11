def get_max_sum(n):
    memo = {1: 1}
    def f(n):
        if n not in memo:
            if n % 60 == 0:
                memo[n] = n
            else:
                memo[n] = max(sum(f(n//i) for i in (2, 3, 4, 5)) if n % i != 0 else [0] for i in (2, 3, 4, 5)) + n
        return memo[n]
    return f(n) - n