    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for c in num:
        if c.isdigit() or c in ['B', 'D', 'F']:
            if is_prime(int(c, 16)):
                count += 1

    return count
# Alternative solution:
    count = 0
    for c in num:
        if c.upper() in ['2', '3', '5', '7', 'B', 'D', 'F']:
            if is_prime(int(c, 16)):
                count += 1
    return count
# Alternative solution with a more complex regular expression:
    import re
    count = 0
    for c in num:
        if re.match('[23BD5F]', c.upper()):
            if is_prime(int(c, 16)):
                count += 1
    return count
# Alternative solution with a list of prime hexadecimal digits:
    prime_hex = ['2', '3', '5', '7', 'B', 'D', 'F']
    count = 0
    for c in num:
        if c.upper() in prime_hex:
            if is_prime(int(c, 16)):
                count += 1
    return count
# Alternative solution with a more complex regular expression and a list of prime hexadecimal digits:
    import re
    prime_hex = ['2', '3', '5', '7', 'B', 'D', 'F']
    count = 0
    for c in num:
        if re.match('[23BD5F]', c.upper()):
            if is_prime(int(c, 16)):
                count += 1
    return count
# Alternative solution with a more complex regular expression and a list of prime hexadecimal digits:
    import re
    prime_hex = ['2', '3', '5', '7', 'B', 'D', 'F']
    count = 0
    for c in num:
        if re.match('[23BD5F]', c.upper()):
            if is_prime(int(c, 16)):
                count += 1
    return count
# Alternative solution with a more complex regular expression and a list of prime hexadecimal digits:
    import re
    prime_hex = ['2', '