def filter_data(data,min_height,min_weight):
    filtered_data = {}
    for name, (height, weight) in data.items():
        if height > min_height and weight > min_weight:
            filtered_data[name] = (height, weight)
    return filtered_data