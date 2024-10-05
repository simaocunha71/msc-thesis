    result = []
    for length in range(1, len(string) + 1):
        result.append(string[:length])

    return result
# or
    return [string[:i] for i in range(1, len(string) + 1)]


