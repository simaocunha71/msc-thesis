
    largest = None
    for i in lst:
        if is_prime(i) and (largest is None or i > largest):
            largest = i
    if largest is None:
        return 0
    else:
        return sum(map(int, str(largest)))


