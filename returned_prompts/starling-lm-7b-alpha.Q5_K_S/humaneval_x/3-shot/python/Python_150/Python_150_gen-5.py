    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


