def get_max_sum(n: int) -> int:
    def f(n):
        if n == 1:
            return n
        return max(f(n // 2) + f(n // 3) + f(n // 4) + f(n // 5), n)
    return f(n)