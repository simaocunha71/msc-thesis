def filter_data(data,min_height, min_weight):
    return {key:value for key,value in data.items() if value[0]>min_height and value[1]>min_weight}