    result = [n]
    current_number = n

    while current_number > 1:
        current_number += 2
        result.append(current_number)

    return result[::-1]