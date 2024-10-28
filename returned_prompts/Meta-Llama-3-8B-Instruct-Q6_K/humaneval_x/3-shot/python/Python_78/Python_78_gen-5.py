    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    count = 0
    for char in num:
        if char.isdigit():
            if int(char) == 2 or int(char) == 3 or int(char) == 5 or int(char) == 7:
                count += 1
        elif char.upper() == 'B':
            count += 1
        elif char.upper() == 'D':
            count += 1

    return count


