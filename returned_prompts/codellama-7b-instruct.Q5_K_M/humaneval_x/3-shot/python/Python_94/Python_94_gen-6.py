    import math

    def prime_check(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    result = 0
    largest_prime = 0
    for num in lst:
        if prime_check(num) and num > largest_prime:
            largest_prime = num

    while largest_prime > 0:
        result += largest_prime % 10
        largest_prime //= 10

    return result


