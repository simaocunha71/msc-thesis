    result = []
    current_number = n

    while current_number != 1:
        if current_number % 2 == 1:
            result.append(current_number)
        current_number = (current_number // 2) if current_number % 2 == 0 else 3 * current_number + 1

    return sorted(result)


