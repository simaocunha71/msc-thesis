    result = []
    current_number = n
    while current_number != 1:
        if current_number % 2 == 1:
            result.append(current_number)
        current_number = collatz(current_number)

    return sorted(result)


