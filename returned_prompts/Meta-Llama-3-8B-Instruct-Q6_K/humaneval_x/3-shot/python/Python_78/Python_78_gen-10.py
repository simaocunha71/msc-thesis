    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if is_prime(int(digit, 16)):
            count += 1
    return count


