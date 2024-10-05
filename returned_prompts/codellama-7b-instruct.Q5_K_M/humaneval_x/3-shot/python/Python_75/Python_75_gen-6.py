    if a < 100:
        for i in range(3, 10):
            if a % i == 0:
                if is_prime(i) and is_prime(a // i):
                    return True
        return False
    else:
        return False


