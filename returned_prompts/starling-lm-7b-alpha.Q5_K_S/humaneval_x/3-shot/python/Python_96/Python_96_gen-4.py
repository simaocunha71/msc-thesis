    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result


