    def has_even_digits(n):
        return any(digit % 2 == 0 for digit in str(n))

    result = [x for x in x if not has_even_digits(x)]
    result.sort()

    return result


