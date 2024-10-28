    histogram = {}
    for char in test:
        if char not in histogram:
            histogram[char] = 1
        else:
            histogram[char] += 1
    return histogram


