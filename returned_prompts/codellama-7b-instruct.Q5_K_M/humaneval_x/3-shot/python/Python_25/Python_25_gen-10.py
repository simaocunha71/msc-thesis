    factors = []
    current_number = n

    for i in range(2, int(n ** 0.5) + 1):
        while current_number % i == 0:
            factors.append(i)
            current_number //= i

    if current_number > 1:
        factors.append(current_number)

    return factors


