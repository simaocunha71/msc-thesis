    def prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = int(num ** 0.5) + 1
        for divisor in range(3, sqrt_num, 2):
            if num % divisor == 0:
                return False
        return True

    result = []
    for i in range(2, n + 1):
        if prime(i):
            result.append(i)
    return result


