def filter_data(data, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in data.items() if height >= min_height and weight >= min_weight}
