def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            count += 1
            a //= i
            if count > 3:
                return False
    return count == 3

print(is_multiply_prime(30))  # True
print(is_multiply_prime(100))  # False
print(is_multiply_prime(1))  # False