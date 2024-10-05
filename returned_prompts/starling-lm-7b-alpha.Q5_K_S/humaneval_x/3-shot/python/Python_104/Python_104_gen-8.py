    def is_even(n):
        while n:
            if n % 2 == 0:
                return True
            n //= 10
        return False

    def has_even_digit(n):
        while n:
            if is_even(n % 10):
                return True
            n //= 10
        return False

    result = []
    for elem in x:
        if not has_even_digit(elem):
            result.append(elem)
    return sorted(result)


