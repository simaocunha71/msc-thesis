    histogram_dict = {}
    for char in test:
        if char in histogram_dict:
            histogram_dict[char] += 1
        else:
            histogram_dict[char] = 1
    max_value = max(histogram_dict.values())
    result = {key: value for key, value in histogram_dict.items() if value == max_value}
    return result


