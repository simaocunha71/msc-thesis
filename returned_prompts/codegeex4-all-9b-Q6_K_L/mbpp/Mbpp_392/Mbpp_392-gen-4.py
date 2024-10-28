def get_max_sum(n):
    cache = {}
    def f(n):
        if n in cache:
            return cache[n]
        cache[n] = max((f(n // 2) + f(n // 3) + f(n // 4) + f(n // 5)), n)
        return cache[n]
    return f(n)

