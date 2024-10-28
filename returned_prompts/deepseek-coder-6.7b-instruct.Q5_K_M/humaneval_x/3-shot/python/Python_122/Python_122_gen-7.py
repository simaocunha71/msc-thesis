    return sum(x for x in arr[:k] if x // 100 == 0 or x // 10 % 10 == 0 or x % 10 == 0)

