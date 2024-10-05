
def is_multiply_prime(a):
    for i in range(2, 10):
        if a % i == 0:
            count = 0
            while a % i == 0:
                a //= i
                count += 1
            if count == 3:
                return True
    return False

