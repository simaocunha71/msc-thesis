    result = {}
    counts = {}

    for letter in test.split():
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1

    for key, value in counts.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)

    return result


