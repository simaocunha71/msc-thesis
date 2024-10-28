def filter_data(dictionary, height, weight):
    result = {}
    for key, value in dictionary.items():
        if value[0] > height and value[1] > weight:
            result[key] = value
    return result