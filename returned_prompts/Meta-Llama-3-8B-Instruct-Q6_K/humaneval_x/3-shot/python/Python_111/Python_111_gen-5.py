    if not test:
        return {}

    frequency = {}
    for char in test.split():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max_count = max(frequency.values())
    result = {char: count for char, count in frequency.items() if count == max_count}

    return result


