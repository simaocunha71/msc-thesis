def get_max_sum(n):
    memo = {1: 1}
    max_sum = 0

    def f(n):
        if n not in memo:
            if n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0:
                memo[n] = max(f(n//2) + f(n//3) + f(n//4) + f(n//5), n)
            else:
                memo[n] = max(f(n//2), f(n//3), f(n//4), f(n//5), n)
        return memo[n]

    max_sum = f(n)
    return max_sum