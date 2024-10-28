    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        max_div = int(x ** 0.5) + 1
        for i in range(3, max_div, 2):
            if x % i == 0:
                return False
        return True

    prime_nums = {'2', '3', '5', '7', 'B', 'D', 'F'}
    result = 0
    for c in num:
        if c in prime_nums:
            result += 1
    return result


