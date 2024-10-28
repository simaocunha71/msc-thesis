    def even_digit(n):
        return all(d % 2 == 0 for d in str(n))

    def is_between(n, a, b):
        return a <= n <= b

    result = [n for n in range(a, b + 1) if even_digit(n) and is_between(n, a, b)]

    return result


