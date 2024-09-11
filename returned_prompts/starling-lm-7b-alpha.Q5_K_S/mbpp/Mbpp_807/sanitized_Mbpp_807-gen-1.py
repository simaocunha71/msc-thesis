def first_odd(numbers):
    if not numbers:
        return None
    for n in numbers:
        if n % 2 != 0:
            return n