def filter_data(data,min_height,min_weight):
    filtered_data = {}
    for key,val in data.items():
        if val[0] > min_height and val[1] > min_weight:
            filtered_data[key] = val
    return filtered_data