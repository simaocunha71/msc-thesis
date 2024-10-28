def filter_data(data, height, weight):
    return {k: v for k, v in data.items() if v[0] >= height and v[1] >= weight}