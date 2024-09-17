def get_ludic(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_ludic(num):
        if num < 6:
            return False
        return is_prime(num - 2) and is_prime(num + 2)

    return [i for i in range(1, n+1) if is_ludic(i)]