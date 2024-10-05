    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            if is_prime(i):
                factors.append(i)
            if is_prime(a//i):
                factors.append(a//i)
    factors = list(set(factors))
    factors.sort()

    if len(factors) < 3:
        return False
    if factors[0]*factors[1]*factors[2] == a:
        return True
    return False


