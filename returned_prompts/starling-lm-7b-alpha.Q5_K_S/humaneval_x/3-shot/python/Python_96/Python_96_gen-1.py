    def check_prime(n):
        if n < 2:
            return False
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True

    result = []
    for i in range(n):
        if check_prime(i):
            result.append(i)
    return result




