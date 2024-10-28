def filter_data(data, min_height, min_weight):
  result = {name: info for name, info in data.items() if info[0] >= min_height and info[1] >= min_weight}
  return result

