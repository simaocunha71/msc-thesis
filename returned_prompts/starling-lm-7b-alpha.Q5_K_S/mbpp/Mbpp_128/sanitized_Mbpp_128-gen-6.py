def long_words(n, string):
    list = string.split()
    result = []
    for i in list:
        if len(i) > n:
            result.append(i)
    return result