    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for c in num:
        if c.isdigit():
            if int(c) in [2, 3, 5, 7]:
                count += 1
        elif c in ['B', 'D', 'F']:
            if is_prime(int(c, 16)):
                count += 1
    return count


