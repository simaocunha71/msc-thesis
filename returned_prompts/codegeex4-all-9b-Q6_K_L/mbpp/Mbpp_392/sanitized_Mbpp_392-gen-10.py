def get_max_sum(n):
    cache = {}
    
    def max_sum(n):
        if n in cache:
            return cache[n]
        if n < 2:
            return n
        cache[n] = max(n, max_sum(n // 2) + max_sum(n // 3) + max_sum(n // 4) + max_sum(n // 5))
        return cache[n]
    
    return max_sum(n)