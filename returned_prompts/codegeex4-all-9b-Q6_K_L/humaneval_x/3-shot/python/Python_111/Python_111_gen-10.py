    result = {}

    for char in test:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    max_value = max(result.values())
    max_keys = [k for k, v in result.items() if v == max_value]

    return {key: max_value for key in max_keys}

