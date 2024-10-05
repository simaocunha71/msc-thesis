    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    length = len(string)
    if is_prime(length):
        return True
    else:
        return False


