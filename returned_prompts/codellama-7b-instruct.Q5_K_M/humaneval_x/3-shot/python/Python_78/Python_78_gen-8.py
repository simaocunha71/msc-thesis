    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5):
            if n % (i * 6 + 1) == 0 or n % (i * 6 + 5) == 0:
                return False
        return True

    count = 0
    for char in num:
        if is_prime(int(char, 16)):
            count += 1
    return count

