    result = [numbers[0]]

    for idx, elem in enumerate(numbers[1:]):
        result.append(max(result[idx], elem))

    return result


