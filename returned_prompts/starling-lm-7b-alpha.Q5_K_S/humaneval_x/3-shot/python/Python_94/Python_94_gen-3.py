    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def sum_of_digits(n):
        result = 0
        while n:
            result += n % 10
            n //= 10
        return result

    max_prime = 0
    for i in lst:
        if is_prime(i) and i > max_prime:
            max_prime = i

    return sum_of_digits(max_prime)


