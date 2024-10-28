    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


