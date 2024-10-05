    def is_prime(n):
        if n < 2: return False
        if n == 2: return True
        if n % 2 == 0: return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0: return False
        return True

    def multiply_three_prime(a):
        if is_prime(a):
            return True
        if a%2==0:
            return False
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a%i==0:
                return False
        return True

    return is_prime(a) and multiply_three_prime(a)


