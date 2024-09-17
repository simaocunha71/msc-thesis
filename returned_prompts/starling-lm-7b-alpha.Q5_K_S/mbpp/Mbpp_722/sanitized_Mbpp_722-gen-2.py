def filter_data(data,min_height,min_weight):
    result = {}
    for key,value in data.items():
        if value[0] > min_height and value[1] > min_weight:
            result[key] = value
    return result