    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        return sum(map(int, str(n)))

    max_prime = max(lst, key=sum_of_digits)
    while not is_prime(max_prime):
        max_prime -= 1

    return sum_of_digits(max_prime)


