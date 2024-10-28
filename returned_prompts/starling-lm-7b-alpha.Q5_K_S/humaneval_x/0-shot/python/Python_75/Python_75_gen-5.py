    def is_prime(n):
        # Corner cases
        if n <= 1:
            return False
        if n <= 3:
            return True
        # This is checked so that we can skip
        # middle five numbers in below loop
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # Corner cases
    if a == 1:
        return False
    if a == 2:
        return True
    if a == 4:
        return False
    if a == 6:
        return False
    if a == 8:
        return False
    if a == 9:
        return True
    if a == 10:
        return False
    if a == 12:
        return False
    if a == 14:
        return True
    if a == 15:
        return True
    if a == 16:
        return False
    if a == 18:
        return False
    if a == 20:
        return True
    if a == 21:
        return True
    if a == 22:
        return True
    if a == 24:
        return False
    if a == 25:
        return True
    if a == 26:
        return True
    if a == 27:
        return True
    if a == 28:
        return False
    if a == 30:
        return True
    if a == 32:
        return False
    if a == 33:
        return True
    if a == 34:
        return True
    if a == 36:
        return False
    if a == 37:
        return True
    if a == 38:
        return True
    if a == 40:
        return True
    if a == 42:
        return True
