    result = []

    for i, elem in enumerate(numbers):
        max_elem = elem

        for j in range(i + 1, len(numbers)):
            if numbers[j] > max_elem:
                max_elem = numbers[j]

        result.append(max_elem)

    return result


