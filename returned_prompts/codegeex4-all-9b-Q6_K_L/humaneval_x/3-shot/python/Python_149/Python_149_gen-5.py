    result = [word for word in lst if len(word) % 2 == 0]
    return sorted(result, key=lambda x: (len(x), x))

