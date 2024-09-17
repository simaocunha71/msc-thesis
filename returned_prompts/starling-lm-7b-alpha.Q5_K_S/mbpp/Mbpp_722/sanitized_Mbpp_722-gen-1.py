def filter_data(dictionary,min_height,min_weight):
    return {k: v for k, v in dictionary.items() if v[0] > min_height and v[1] > min_weight}