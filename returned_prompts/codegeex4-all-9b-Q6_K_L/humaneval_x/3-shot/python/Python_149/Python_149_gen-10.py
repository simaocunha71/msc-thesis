    result = [word for word in lst if len(word) % 2 == 0]
    result.sort(key=lambda x: (len(x), x))
    return result

