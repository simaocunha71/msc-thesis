def filter_data(data, min_height, min_weight):
  filtered_data = {k: v for k, v in data.items() if v[0] > min_height and v[1] > min_weight}
  return filtered_data