    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = []
    i = 2
    while i < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result


