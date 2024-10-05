    histogram_dict = {}
    for char in test:
        if char not in histogram_dict:
            histogram_dict[char] = 1
        else:
            histogram_dict[char] += 1
    return histogram_dict


