    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        return sum(map(int, str(n)))

    return max(filter(is_prime, lst), key=sum_of_digits)


