def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
    return None