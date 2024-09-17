def extract_singly(t):
    result = []
    for sublist in t:
        for elem in sublist:
            result.append(elem)
    return result