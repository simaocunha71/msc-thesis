def get_max_sum(n):
    memo = {1: 1}

    def f(k):
        if k not in memo:
            if k % 2 == 0 and k % 3 == 0 and k % 4 == 0 and k % 5 == 0:
                memo[k] = max(f(k // 2) + f(k // 3) + f(k // 4) + f(k // 5), k)
            elif k % 2 == 0:
                memo[k] = max(f(k // 2), f(k))
            elif k % 3 == 0:
                memo[k] = max(f(k // 3), f(k))
            elif k % 4 == 0:
                memo[k] = max(f(k // 4), f(k))
            elif k % 5 == 0:
                memo[k] = max(f(k // 5), f(k))
            else:
                memo[k] = f(k)
        return memo[k]

    return f(n)