    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_digits(num):
        return sum(int(digit) for digit in str(num))

    max_prime = max(lst, key=lambda x: is_prime(x))
    return sum_digits(max_prime)


