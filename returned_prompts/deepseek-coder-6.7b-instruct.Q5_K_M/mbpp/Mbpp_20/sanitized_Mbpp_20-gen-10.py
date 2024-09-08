def is_woodall(n):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    factors = list(set(factors))
    for factor in factors:
        if factor*(factor+1) == n:
            return True
    return False