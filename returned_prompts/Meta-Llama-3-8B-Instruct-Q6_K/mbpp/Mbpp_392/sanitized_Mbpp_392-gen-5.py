def get_max_sum(n):
    memo = {}
    def f(n):
        if n in memo:
            return memo[n]
        if n < 10:
            return n
        res = max([f(n//2) + f(n//3) + f(n//4) + f(n//5), n])
        memo[n] = res
        return res
    return f(n)  # or return f(n) if you want the function to return the result directly