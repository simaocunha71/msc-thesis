    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_digits(n):
        return sum(map(int, str(n)))

    result = 0
    for elem in lst:
        if is_prime(elem):
            result += sum_digits(elem)

    return result


