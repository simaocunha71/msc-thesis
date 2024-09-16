def filter_data(data, height, weight):
    return {name: (h, w) for name, (h, w) in data.items() if h > height and w > weight}