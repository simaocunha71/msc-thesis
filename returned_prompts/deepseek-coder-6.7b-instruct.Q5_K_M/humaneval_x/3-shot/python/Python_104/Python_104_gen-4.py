    def has_even_digit(n):
        while n > 0:
            if (n % 10) % 2 == 0:
                return True
            n = n // 10
        return False

    return sorted([i for i in x if not has_even_digit(i)])


