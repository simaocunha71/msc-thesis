    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    hex_map = {'2': True, '3': True, '5': True, '7': True, 'B': True, 'D': True}
    count = 0

    for char in num:
        if char in hex_map:
            count += 1

    return count


