    if not test:
        return {}

    test = test.split()
    max_count = max(len(word) for word in test)
    result = {}

    for word in test:
        for char in set(word):
            if word.count(char) == max_count:
                result[char] = max_count
                break

    return result


