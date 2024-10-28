    if not numbers:
        return (0, 1)

    prod = 1
    for num in numbers:
        prod *= num

    return (sum(numbers), prod)


