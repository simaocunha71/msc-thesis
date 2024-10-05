    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def sum_digits(num):
        result = 0
        while num:
            result += num % 10
            num //= 10
        return result

    max_prime = max(filter(is_prime, lst))
    return sum_digits(max_prime)


