    result = 1
    is_even = True

    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            result *= digit
            is_even = False

        n //= 10

    return result if not is_even else 0

