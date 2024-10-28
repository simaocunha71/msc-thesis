    largest_prime = 0

    for num in lst:
        if num > largest_prime:
            largest_prime = num

    result = 0
    while largest_prime > 0:
        result += largest_prime % 10
        largest_prime //= 10

    return result


