    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        result = 0
        while n:
            result += n % 10
            n //= 10
        return result

    max_prime = max(lst)
    while not is_prime(max_prime):
        max_prime -= 1
    return sum_of_digits(max_prime)


