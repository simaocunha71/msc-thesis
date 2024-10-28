    result = []

    for i in range(len(numbers)):
        current_max = numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[j] > current_max:
                current_max = numbers[j]

        result.append(current_max)

    return result


